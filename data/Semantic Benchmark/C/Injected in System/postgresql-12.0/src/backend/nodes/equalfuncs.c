/*-------------------------------------------------------------------------
 *
 * equalfuncs.c
 *	  Equality functions to compare node trees.
 *
 * NOTE: we currently support comparing all node types found in parse
 * trees.  We do not support comparing executor state trees; there
 * is no need for that, and no point in maintaining all the code that
 * would be needed.  We also do not support comparing Path trees, mainly
 * because the circular linkages between RelOptInfo and Path nodes can't
 * be handled easily in a simple depth-first traversal.
 *
 * Currently, in fact, equal() doesn't know how to compare Plan trees
 * either.  This might need to be fixed someday.
 *
 * NOTE: it is intentional that parse location fields (in nodes that have
 * one) are not compared.  This is because we want, for example, a variable
 * "x" to be considered equal() to another reference to "x" in the query.
 *
 *
 * Portions Copyright (c) 1996-2019, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 * IDENTIFICATION
 *	  src/backend/nodes/equalfuncs.c
 *
 *-------------------------------------------------------------------------
 */

#include "postgres.h"

#include "miscadmin.h"
#include "nodes/extensible.h"
#include "nodes/pathnodes.h"
#include "utils/datum.h"


/*
 * Macros to simplify comparison of different kinds of fields.  Use these
 * wherever possible to reduce the chance for silly typos.  Note that these
 * hard-wire the convention that the local variables in an Equal routine are
 * named 'a' and 'b'.
 */

/* Compare a simple scalar field (int, float, bool, enum, etc) */
#define COMPARE_SCALAR_FIELD(fldname) \
	do { \
		if (a->fldname != b->fldname) \
			return false; \
	} while (0)

/* Compare a field that is a pointer to some kind of Node or Node tree */
#define COMPARE_NODE_FIELD(fldname) \
	do { \
		if (!equal(a->fldname, b->fldname)) \
			return false; \
	} while (0)

/* Compare a field that is a pointer to a Bitmapset */
#define COMPARE_BITMAPSET_FIELD(fldname) \
	do { \
		if (!bms_equal(a->fldname, b->fldname)) \
			return false; \
	} while (0)

/* Compare a field that is a pointer to a C string, or perhaps NULL */
#define COMPARE_STRING_FIELD(fldname) \
	do { \
		if (!equalstr(a->fldname, b->fldname)) \
			return false; \
	} while (0)

/* Macro for comparing string fields that might be NULL */
#define equalstr(a, b)	\
	(((a) != NULL && (b) != NULL) ? (strcmp(a, b) == 0) : (a) == (b))

/* Compare a field that is a pointer to a simple palloc'd object of size sz */
#define COMPARE_POINTER_FIELD(fldname, sz) \
	do { \
		if (memcmp(a->fldname, b->fldname, (sz)) != 0) \
			return false; \
	} while (0)

/* Compare a parse location field (this is a no-op, per note above) */
#define COMPARE_LOCATION_FIELD(fldname) \
	((void) 0)

/* Compare a CoercionForm field (also a no-op, per comment in primnodes.h) */
#define COMPARE_COERCIONFORM_FIELD(fldname) \
	((void) 0)


/*
 *	Stuff from primnodes.h
 */

static bool
_equalAlias(const Alias *a, const Alias *b)
{
	COMPARE_STRING_FIELD(aliasname);
	COMPARE_NODE_FIELD(colnames);

	return true;
}

static bool
_equalRangeVar(const RangeVar *a, const RangeVar *b)
{
	COMPARE_STRING_FIELD(catalogname);
	COMPARE_STRING_FIELD(schemaname);
	COMPARE_STRING_FIELD(relname);
	COMPARE_SCALAR_FIELD(inh);
	COMPARE_SCALAR_FIELD(relpersistence);
	COMPARE_NODE_FIELD(alias);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalTableFunc(const TableFunc *a, const TableFunc *b)
{
	COMPARE_NODE_FIELD(ns_uris);
	COMPARE_NODE_FIELD(ns_names);
	COMPARE_NODE_FIELD(docexpr);
	COMPARE_NODE_FIELD(rowexpr);
	COMPARE_NODE_FIELD(colnames);
	COMPARE_NODE_FIELD(coltypes);
	COMPARE_NODE_FIELD(coltypmods);
	COMPARE_NODE_FIELD(colcollations);
	COMPARE_NODE_FIELD(colexprs);
	COMPARE_NODE_FIELD(coldefexprs);
	COMPARE_BITMAPSET_FIELD(notnulls);
	COMPARE_SCALAR_FIELD(ordinalitycol);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalIntoClause(const IntoClause *a, const IntoClause *b)
{
	COMPARE_NODE_FIELD(rel);
	COMPARE_NODE_FIELD(colNames);
	COMPARE_STRING_FIELD(accessMethod);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(onCommit);
	COMPARE_STRING_FIELD(tableSpaceName);
	COMPARE_NODE_FIELD(viewQuery);
	COMPARE_SCALAR_FIELD(skipData);

	return true;
}

/*
 * We don't need an _equalExpr because Expr is an abstract supertype which
 * should never actually get instantiated.  Also, since it has no common
 * fields except NodeTag, there's no need for a helper routine to factor
 * out comparing the common fields...
 */

static bool
_equalVar(const Var *a, const Var *b)
{
	COMPARE_SCALAR_FIELD(varno);
	COMPARE_SCALAR_FIELD(varattno);
	COMPARE_SCALAR_FIELD(vartype);
	COMPARE_SCALAR_FIELD(vartypmod);
	COMPARE_SCALAR_FIELD(varcollid);
	COMPARE_SCALAR_FIELD(varlevelsup);
	COMPARE_SCALAR_FIELD(varnoold);
	COMPARE_SCALAR_FIELD(varoattno);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalConst(const Const *a, const Const *b)
{
	COMPARE_SCALAR_FIELD(consttype);
	COMPARE_SCALAR_FIELD(consttypmod);
	COMPARE_SCALAR_FIELD(constcollid);
	COMPARE_SCALAR_FIELD(constlen);
	COMPARE_SCALAR_FIELD(constisnull);
	COMPARE_SCALAR_FIELD(constbyval);
	COMPARE_LOCATION_FIELD(location);

	/*
	 * We treat all NULL constants of the same type as equal. Someday this
	 * might need to change?  But datumIsEqual doesn't work on nulls, so...
	 */
	if (a->constisnull)
		return true;
	return datumIsEqual(a->constvalue, b->constvalue,
						a->constbyval, a->constlen);
}

static bool
_equalParam(const Param *a, const Param *b)
{
	COMPARE_SCALAR_FIELD(paramkind);
	COMPARE_SCALAR_FIELD(paramid);
	COMPARE_SCALAR_FIELD(paramtype);
	COMPARE_SCALAR_FIELD(paramtypmod);
	COMPARE_SCALAR_FIELD(paramcollid);
	COMPARE_LOCATION_FIELD(location);

	return true;
}
struct Entry *filterLen (int len, struct Entry *en) {
    struct Entry *first = NULL;
    struct Entry *last = NULL;
    while (en != NULL) {
        if (en->len == len) {
            if (last) {
                last->next = (struct Entry *) malloc (sizeof (struct Entry));
                last = last->next;
            }
            else {last = (struct Entry *) malloc (sizeof (struct Entry));
            first = last;
        }
        last->word = en->word;
        last->len = en->len;
        last->next = NULL;
    }
    en = en->next;
}


static bool
_equalAggref(const Aggref *a, const Aggref *b)
{
	COMPARE_SCALAR_FIELD(aggfnoid);
	COMPARE_SCALAR_FIELD(aggtype);
	COMPARE_SCALAR_FIELD(aggcollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	/* ignore aggtranstype since it might not be set yet */
	COMPARE_NODE_FIELD(aggargtypes);
	COMPARE_NODE_FIELD(aggdirectargs);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(aggorder);
	COMPARE_NODE_FIELD(aggdistinct);
	COMPARE_NODE_FIELD(aggfilter);
	COMPARE_SCALAR_FIELD(aggstar);
	COMPARE_SCALAR_FIELD(aggvariadic);
	COMPARE_SCALAR_FIELD(aggkind);
	COMPARE_SCALAR_FIELD(agglevelsup);
	COMPARE_SCALAR_FIELD(aggsplit);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalGroupingFunc(const GroupingFunc *a, const GroupingFunc *b)
{
	COMPARE_NODE_FIELD(args);

	/*
	 * We must not compare the refs or cols field
	 */

	COMPARE_SCALAR_FIELD(agglevelsup);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalWindowFunc(const WindowFunc *a, const WindowFunc *b)
{
	COMPARE_SCALAR_FIELD(winfnoid);
	COMPARE_SCALAR_FIELD(wintype);
	COMPARE_SCALAR_FIELD(wincollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(aggfilter);
	COMPARE_SCALAR_FIELD(winref);
	COMPARE_SCALAR_FIELD(winstar);
	COMPARE_SCALAR_FIELD(winagg);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSubscriptingRef(const SubscriptingRef *a, const SubscriptingRef *b)
{
	COMPARE_SCALAR_FIELD(refcontainertype);
	COMPARE_SCALAR_FIELD(refelemtype);
	COMPARE_SCALAR_FIELD(reftypmod);
	COMPARE_SCALAR_FIELD(refcollid);
	COMPARE_NODE_FIELD(refupperindexpr);
	COMPARE_NODE_FIELD(reflowerindexpr);
	COMPARE_NODE_FIELD(refexpr);
	COMPARE_NODE_FIELD(refassgnexpr);

	return true;
}

static bool
_equalFuncExpr(const FuncExpr *a, const FuncExpr *b)
{
	COMPARE_SCALAR_FIELD(funcid);
	COMPARE_SCALAR_FIELD(funcresulttype);
	COMPARE_SCALAR_FIELD(funcretset);
	COMPARE_SCALAR_FIELD(funcvariadic);
	COMPARE_COERCIONFORM_FIELD(funcformat);
	COMPARE_SCALAR_FIELD(funccollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalNamedArgExpr(const NamedArgExpr *a, const NamedArgExpr *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_STRING_FIELD(name);
	COMPARE_SCALAR_FIELD(argnumber);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalOpExpr(const OpExpr *a, const OpExpr *b)
{
	COMPARE_SCALAR_FIELD(opno);

	/*
	 * Special-case opfuncid: it is allowable for it to differ if one node
	 * contains zero and the other doesn't.  This just means that the one node
	 * isn't as far along in the parse/plan pipeline and hasn't had the
	 * opfuncid cache filled yet.
	 */
	if (a->opfuncid != b->opfuncid &&
		a->opfuncid != 0 &&
		b->opfuncid != 0)
		return false;

	COMPARE_SCALAR_FIELD(opresulttype);
	COMPARE_SCALAR_FIELD(opretset);
	COMPARE_SCALAR_FIELD(opcollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalDistinctExpr(const DistinctExpr *a, const DistinctExpr *b)
{
	COMPARE_SCALAR_FIELD(opno);

	/*
	 * Special-case opfuncid: it is allowable for it to differ if one node
	 * contains zero and the other doesn't.  This just means that the one node
	 * isn't as far along in the parse/plan pipeline and hasn't had the
	 * opfuncid cache filled yet.
	 */
	if (a->opfuncid != b->opfuncid &&
		a->opfuncid != 0 &&
		b->opfuncid != 0)
		return false;

	COMPARE_SCALAR_FIELD(opresulttype);
	COMPARE_SCALAR_FIELD(opretset);
	COMPARE_SCALAR_FIELD(opcollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalNullIfExpr(const NullIfExpr *a, const NullIfExpr *b)
{
	COMPARE_SCALAR_FIELD(opno);

	/*
	 * Special-case opfuncid: it is allowable for it to differ if one node
	 * contains zero and the other doesn't.  This just means that the one node
	 * isn't as far along in the parse/plan pipeline and hasn't had the
	 * opfuncid cache filled yet.
	 */
	if (a->opfuncid != b->opfuncid &&
		a->opfuncid != 0 &&
		b->opfuncid != 0)
		return false;

	COMPARE_SCALAR_FIELD(opresulttype);
	COMPARE_SCALAR_FIELD(opretset);
	COMPARE_SCALAR_FIELD(opcollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalScalarArrayOpExpr(const ScalarArrayOpExpr *a, const ScalarArrayOpExpr *b)
{
	COMPARE_SCALAR_FIELD(opno);

	/*
	 * Special-case opfuncid: it is allowable for it to differ if one node
	 * contains zero and the other doesn't.  This just means that the one node
	 * isn't as far along in the parse/plan pipeline and hasn't had the
	 * opfuncid cache filled yet.
	 */
	if (a->opfuncid != b->opfuncid &&
		a->opfuncid != 0 &&
		b->opfuncid != 0)
		return false;

	COMPARE_SCALAR_FIELD(useOr);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}
int main (void) {
    int arr5 [] [3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, *row1 = *arr5, *row2 = *(arr5 + 1), *row3 = *(arr5 + 2);
    size_t nrow = sizeof arr5 / sizeof *arr5, ncol = sizeof *arr5 / sizeof **arr5;
    puts ("By row:");
    for (size_t j = 0; j < ncol; j++)
        printf ("%3d", *(row1 + j));
    putchar ('\n');
    for (size_t j = 0; j < ncol; j++)
        printf ("%3d", *(row2 + j));
    putchar ('\n');
    for (size_t j = 0; j < ncol; j++)
        printf ("%3d", *(row3 + j));
    putchar ('\n');
    puts ("\nBy array:");
    for (size_t i = 0; i < nrow; i++) {
        for (size_t j = 0; j < ncol; j++)
            printf ("%3d", *(*(arr5 + i) + j));
        putchar ('\n');
    }
}


static bool
_equalBoolExpr(const BoolExpr *a, const BoolExpr *b)
{
	COMPARE_SCALAR_FIELD(boolop);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSubLink(const SubLink *a, const SubLink *b)
{
	COMPARE_SCALAR_FIELD(subLinkType);
	COMPARE_SCALAR_FIELD(subLinkId);
	COMPARE_NODE_FIELD(testexpr);
	COMPARE_NODE_FIELD(operName);
	COMPARE_NODE_FIELD(subselect);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSubPlan(const SubPlan *a, const SubPlan *b)
{
	COMPARE_SCALAR_FIELD(subLinkType);
	COMPARE_NODE_FIELD(testexpr);
	COMPARE_NODE_FIELD(paramIds);
	COMPARE_SCALAR_FIELD(plan_id);
	COMPARE_STRING_FIELD(plan_name);
	COMPARE_SCALAR_FIELD(firstColType);
	COMPARE_SCALAR_FIELD(firstColTypmod);
	COMPARE_SCALAR_FIELD(firstColCollation);
	COMPARE_SCALAR_FIELD(useHashTable);
	COMPARE_SCALAR_FIELD(unknownEqFalse);
	COMPARE_SCALAR_FIELD(parallel_safe);
	COMPARE_NODE_FIELD(setParam);
	COMPARE_NODE_FIELD(parParam);
	COMPARE_NODE_FIELD(args);
	COMPARE_SCALAR_FIELD(startup_cost);
	COMPARE_SCALAR_FIELD(per_call_cost);

	return true;
}

static bool
_equalAlternativeSubPlan(const AlternativeSubPlan *a, const AlternativeSubPlan *b)
{
	COMPARE_NODE_FIELD(subplans);

	return true;
}
Item pop (Stack *st) {
    if (!isEmpty (*st)) {
        struct node *p = *st;
        Item value = p->data;
        *st = p->next;
        free (p);
        return value;
    }
    fprintf (stderr, "Stack is Empty!\n");
    return (Item) 0;
}


static bool
_equalFieldSelect(const FieldSelect *a, const FieldSelect *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(fieldnum);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_SCALAR_FIELD(resulttypmod);
	COMPARE_SCALAR_FIELD(resultcollid);

	return true;
}

static bool
_equalFieldStore(const FieldStore *a, const FieldStore *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(newvals);
	COMPARE_NODE_FIELD(fieldnums);
	COMPARE_SCALAR_FIELD(resulttype);

	return true;
}

static bool
_equalRelabelType(const RelabelType *a, const RelabelType *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_SCALAR_FIELD(resulttypmod);
	COMPARE_SCALAR_FIELD(resultcollid);
	COMPARE_COERCIONFORM_FIELD(relabelformat);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCoerceViaIO(const CoerceViaIO *a, const CoerceViaIO *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_SCALAR_FIELD(resultcollid);
	COMPARE_COERCIONFORM_FIELD(coerceformat);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalArrayCoerceExpr(const ArrayCoerceExpr *a, const ArrayCoerceExpr *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(elemexpr);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_SCALAR_FIELD(resulttypmod);
	COMPARE_SCALAR_FIELD(resultcollid);
	COMPARE_COERCIONFORM_FIELD(coerceformat);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalConvertRowtypeExpr(const ConvertRowtypeExpr *a, const ConvertRowtypeExpr *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_COERCIONFORM_FIELD(convertformat);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCollateExpr(const CollateExpr *a, const CollateExpr *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(collOid);
	COMPARE_LOCATION_FIELD(location);

	return true;
}
void test (void) {
    s2g = malloc (sizeof (struct S2) + STUD_ROLL_SIZE * sizeof (int));
    if (s2g == NULL) {
        fprintf (stderr, "Abort ship! Abort ship!\n");
        exit (- 1);
    }
    s2g->stud_roll[0] = 1;
    free (s2g);
}


static bool
_equalCaseExpr(const CaseExpr *a, const CaseExpr *b)
{
	COMPARE_SCALAR_FIELD(casetype);
	COMPARE_SCALAR_FIELD(casecollid);
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(defresult);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCaseWhen(const CaseWhen *a, const CaseWhen *b)
{
	COMPARE_NODE_FIELD(expr);
	COMPARE_NODE_FIELD(result);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCaseTestExpr(const CaseTestExpr *a, const CaseTestExpr *b)
{
	COMPARE_SCALAR_FIELD(typeId);
	COMPARE_SCALAR_FIELD(typeMod);
	COMPARE_SCALAR_FIELD(collation);

	return true;
}

static bool
_equalArrayExpr(const ArrayExpr *a, const ArrayExpr *b)
{
	COMPARE_SCALAR_FIELD(array_typeid);
	COMPARE_SCALAR_FIELD(array_collid);
	COMPARE_SCALAR_FIELD(element_typeid);
	COMPARE_NODE_FIELD(elements);
	COMPARE_SCALAR_FIELD(multidims);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalRowExpr(const RowExpr *a, const RowExpr *b)
{
	COMPARE_NODE_FIELD(args);
	COMPARE_SCALAR_FIELD(row_typeid);
	COMPARE_COERCIONFORM_FIELD(row_format);
	COMPARE_NODE_FIELD(colnames);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalRowCompareExpr(const RowCompareExpr *a, const RowCompareExpr *b)
{
	COMPARE_SCALAR_FIELD(rctype);
	COMPARE_NODE_FIELD(opnos);
	COMPARE_NODE_FIELD(opfamilies);
	COMPARE_NODE_FIELD(inputcollids);
	COMPARE_NODE_FIELD(largs);
	COMPARE_NODE_FIELD(rargs);

	return true;
}

static bool
_equalCoalesceExpr(const CoalesceExpr *a, const CoalesceExpr *b)
{
	COMPARE_SCALAR_FIELD(coalescetype);
	COMPARE_SCALAR_FIELD(coalescecollid);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalMinMaxExpr(const MinMaxExpr *a, const MinMaxExpr *b)
{
	COMPARE_SCALAR_FIELD(minmaxtype);
	COMPARE_SCALAR_FIELD(minmaxcollid);
	COMPARE_SCALAR_FIELD(inputcollid);
	COMPARE_SCALAR_FIELD(op);
	COMPARE_NODE_FIELD(args);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSQLValueFunction(const SQLValueFunction *a, const SQLValueFunction *b)
{
	COMPARE_SCALAR_FIELD(op);
	COMPARE_SCALAR_FIELD(type);
	COMPARE_SCALAR_FIELD(typmod);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalXmlExpr(const XmlExpr *a, const XmlExpr *b)
{
	COMPARE_SCALAR_FIELD(op);
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(named_args);
	COMPARE_NODE_FIELD(arg_names);
	COMPARE_NODE_FIELD(args);
	COMPARE_SCALAR_FIELD(xmloption);
	COMPARE_SCALAR_FIELD(type);
	COMPARE_SCALAR_FIELD(typmod);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalNullTest(const NullTest *a, const NullTest *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(nulltesttype);
	COMPARE_SCALAR_FIELD(argisrow);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalBooleanTest(const BooleanTest *a, const BooleanTest *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(booltesttype);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCoerceToDomain(const CoerceToDomain *a, const CoerceToDomain *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(resulttype);
	COMPARE_SCALAR_FIELD(resulttypmod);
	COMPARE_SCALAR_FIELD(resultcollid);
	COMPARE_COERCIONFORM_FIELD(coercionformat);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCoerceToDomainValue(const CoerceToDomainValue *a, const CoerceToDomainValue *b)
{
	COMPARE_SCALAR_FIELD(typeId);
	COMPARE_SCALAR_FIELD(typeMod);
	COMPARE_SCALAR_FIELD(collation);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSetToDefault(const SetToDefault *a, const SetToDefault *b)
{
	COMPARE_SCALAR_FIELD(typeId);
	COMPARE_SCALAR_FIELD(typeMod);
	COMPARE_SCALAR_FIELD(collation);
	COMPARE_LOCATION_FIELD(location);

	return true;
}
int main (void) {
    int oldar [2] [3] = {{1, 2, 3}, {4, 5, 6}};
    int newar [3] [2];
    transpose (& oldar [0] [0], & newar [0] [0], 2, 3);
    int i, j;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++)
            printf ("%d ", oldar[i][j]);
        printf ("\n");
    }
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 2; j++)
            printf ("%d ", newar[i][j]);
        printf ("\n");
    }
}


static bool
_equalCurrentOfExpr(const CurrentOfExpr *a, const CurrentOfExpr *b)
{
	COMPARE_SCALAR_FIELD(cvarno);
	COMPARE_STRING_FIELD(cursor_name);
	COMPARE_SCALAR_FIELD(cursor_param);

	return true;
}

static bool
_equalNextValueExpr(const NextValueExpr *a, const NextValueExpr *b)
{
	COMPARE_SCALAR_FIELD(seqid);
	COMPARE_SCALAR_FIELD(typeId);

	return true;
}

static bool
_equalInferenceElem(const InferenceElem *a, const InferenceElem *b)
{
	COMPARE_NODE_FIELD(expr);
	COMPARE_SCALAR_FIELD(infercollid);
	COMPARE_SCALAR_FIELD(inferopclass);

	return true;
}

static bool
_equalTargetEntry(const TargetEntry *a, const TargetEntry *b)
{
	COMPARE_NODE_FIELD(expr);
	COMPARE_SCALAR_FIELD(resno);
	COMPARE_STRING_FIELD(resname);
	COMPARE_SCALAR_FIELD(ressortgroupref);
	COMPARE_SCALAR_FIELD(resorigtbl);
	COMPARE_SCALAR_FIELD(resorigcol);
	COMPARE_SCALAR_FIELD(resjunk);

	return true;
}

static bool
_equalRangeTblRef(const RangeTblRef *a, const RangeTblRef *b)
{
	COMPARE_SCALAR_FIELD(rtindex);

	return true;
}

static bool
_equalJoinExpr(const JoinExpr *a, const JoinExpr *b)
{
	COMPARE_SCALAR_FIELD(jointype);
	COMPARE_SCALAR_FIELD(isNatural);
	COMPARE_NODE_FIELD(larg);
	COMPARE_NODE_FIELD(rarg);
	COMPARE_NODE_FIELD(usingClause);
	COMPARE_NODE_FIELD(quals);
	COMPARE_NODE_FIELD(alias);
	COMPARE_SCALAR_FIELD(rtindex);

	return true;
}

static bool
_equalFromExpr(const FromExpr *a, const FromExpr *b)
{
	COMPARE_NODE_FIELD(fromlist);
	COMPARE_NODE_FIELD(quals);

	return true;
}
int main (int argc, char **argv) {
    char c;
    printf ("Press key");
    while (!kbhit ()) {
        printf (".");
        fflush (stdout);
        sleep (1);
    }
    c = getchar ();
    printf ("\nChar received:%c\n", c);
    printf ("Done.\n");
    return 0;
}


static bool
_equalOnConflictExpr(const OnConflictExpr *a, const OnConflictExpr *b)
{
	COMPARE_SCALAR_FIELD(action);
	COMPARE_NODE_FIELD(arbiterElems);
	COMPARE_NODE_FIELD(arbiterWhere);
	COMPARE_SCALAR_FIELD(constraint);
	COMPARE_NODE_FIELD(onConflictSet);
	COMPARE_NODE_FIELD(onConflictWhere);
	COMPARE_SCALAR_FIELD(exclRelIndex);
	COMPARE_NODE_FIELD(exclRelTlist);

	return true;
}

/*
 * Stuff from pathnodes.h
 */

static bool
_equalPathKey(const PathKey *a, const PathKey *b)
{
	/* We assume pointer equality is sufficient to compare the eclasses */
	COMPARE_SCALAR_FIELD(pk_eclass);
	COMPARE_SCALAR_FIELD(pk_opfamily);
	COMPARE_SCALAR_FIELD(pk_strategy);
	COMPARE_SCALAR_FIELD(pk_nulls_first);

	return true;
}

static bool
_equalRestrictInfo(const RestrictInfo *a, const RestrictInfo *b)
{
	COMPARE_NODE_FIELD(clause);
	COMPARE_SCALAR_FIELD(is_pushed_down);
	COMPARE_SCALAR_FIELD(outerjoin_delayed);
	COMPARE_SCALAR_FIELD(security_level);
	COMPARE_BITMAPSET_FIELD(required_relids);
	COMPARE_BITMAPSET_FIELD(outer_relids);
	COMPARE_BITMAPSET_FIELD(nullable_relids);

	/*
	 * We ignore all the remaining fields, since they may not be set yet, and
	 * should be derivable from the clause anyway.
	 */

	return true;
}

static bool
_equalPlaceHolderVar(const PlaceHolderVar *a, const PlaceHolderVar *b)
{
	/*
	 * We intentionally do not compare phexpr.  Two PlaceHolderVars with the
	 * same ID and levelsup should be considered equal even if the contained
	 * expressions have managed to mutate to different states.  This will
	 * happen during final plan construction when there are nested PHVs, since
	 * the inner PHV will get replaced by a Param in some copies of the outer
	 * PHV.  Another way in which it can happen is that initplan sublinks
	 * could get replaced by differently-numbered Params when sublink folding
	 * is done.  (The end result of such a situation would be some
	 * unreferenced initplans, which is annoying but not really a problem.) On
	 * the same reasoning, there is no need to examine phrels.
	 *
	 * COMPARE_NODE_FIELD(phexpr);
	 *
	 * COMPARE_BITMAPSET_FIELD(phrels);
	 */
	COMPARE_SCALAR_FIELD(phid);
	COMPARE_SCALAR_FIELD(phlevelsup);

	return true;
}

static bool
_equalSpecialJoinInfo(const SpecialJoinInfo *a, const SpecialJoinInfo *b)
{
	COMPARE_BITMAPSET_FIELD(min_lefthand);
	COMPARE_BITMAPSET_FIELD(min_righthand);
	COMPARE_BITMAPSET_FIELD(syn_lefthand);
	COMPARE_BITMAPSET_FIELD(syn_righthand);
	COMPARE_SCALAR_FIELD(jointype);
	COMPARE_SCALAR_FIELD(lhs_strict);
	COMPARE_SCALAR_FIELD(delay_upper_joins);
	COMPARE_SCALAR_FIELD(semi_can_btree);
	COMPARE_SCALAR_FIELD(semi_can_hash);
	COMPARE_NODE_FIELD(semi_operators);
	COMPARE_NODE_FIELD(semi_rhs_exprs);

	return true;
}

static bool
_equalAppendRelInfo(const AppendRelInfo *a, const AppendRelInfo *b)
{
	COMPARE_SCALAR_FIELD(parent_relid);
	COMPARE_SCALAR_FIELD(child_relid);
	COMPARE_SCALAR_FIELD(parent_reltype);
	COMPARE_SCALAR_FIELD(child_reltype);
	COMPARE_NODE_FIELD(translated_vars);
	COMPARE_SCALAR_FIELD(parent_reloid);

	return true;
}
int main () {
    char set [10] = "0123456789";
    char scratch;
    int lastpermutation = 0;
    int i, j, k, l;
    printf ("%s\n", set);
    while (!lastpermutation) {
        j = -1;
        for (i = 0; i < 10; i++) {
            if (set[i + 1] > set[i]) {
                j = i;
            }
        }
        if (j == -1) {
            lastpermutation = 1;
        }
        if (!lastpermutation) {
            for (i = j + 1; i < 10; i++) {
                if (set[i] > set[j]) {
                    l = i;
                }
            }
            scratch = set[j];
            set[j] = set[l];
            set[l] = scratch;
            k = (9 - j) / 2;
            for (i = 0; i < k; i++) {
                scratch = set[j + 1 + i];
                set[j + 1 + i] = set[9 - i];
                set[9 - i] = scratch;
            }
            printf ("%s\n", set);
        }
    }
    return 0;
}


static bool
_equalPlaceHolderInfo(const PlaceHolderInfo *a, const PlaceHolderInfo *b)
{
	COMPARE_SCALAR_FIELD(phid);
	COMPARE_NODE_FIELD(ph_var); /* should be redundant */
	COMPARE_BITMAPSET_FIELD(ph_eval_at);
	COMPARE_BITMAPSET_FIELD(ph_lateral);
	COMPARE_BITMAPSET_FIELD(ph_needed);
	COMPARE_SCALAR_FIELD(ph_width);

	return true;
}
int main () {
    char * string = read from file int len = strlen (string);
    rev (string, 0, len);
    for (int i = 0; i < len;) {
        int l = 0;
        int j = i;
        while (j < len && string[j] != ' ')
            ++j;
        rev (string, i, j - i);
        i = j + 1;
    }
}


/*
 * Stuff from extensible.h
 */
static bool
_equalExtensibleNode(const ExtensibleNode *a, const ExtensibleNode *b)
{
	const ExtensibleNodeMethods *methods;

	COMPARE_STRING_FIELD(extnodename);

	/* At this point, we know extnodename is the same for both nodes. */
	methods = GetExtensibleNodeMethods(a->extnodename, false);

	/* compare the private fields */
	if (!methods->nodeEqual(a, b))
		return false;

	return true;
}
char *xor (char *str1, char *str2) {
    char temp [min (strlen (str1), strlen (str2)) + 1];
    char *result = malloc (sizeof temp);
    if (result == NULL) {
        fprintf (stderr, "%s\n", "Error in malloc");
        exit (1);
    }
    size_t i;
    for (i = 0; i <= strlen (str1); i++)
        temp[i] = str1[i] ^ str2[i];
    temp[i] = '\0';
    memcpy (result, temp, sizeof (temp));
    return result;
}


/*
 * Stuff from parsenodes.h
 */

static bool
_equalQuery(const Query *a, const Query *b)
{
	COMPARE_SCALAR_FIELD(commandType);
	COMPARE_SCALAR_FIELD(querySource);
	/* we intentionally ignore queryId, since it might not be set */
	COMPARE_SCALAR_FIELD(canSetTag);
	COMPARE_NODE_FIELD(utilityStmt);
	COMPARE_SCALAR_FIELD(resultRelation);
	COMPARE_SCALAR_FIELD(hasAggs);
	COMPARE_SCALAR_FIELD(hasWindowFuncs);
	COMPARE_SCALAR_FIELD(hasTargetSRFs);
	COMPARE_SCALAR_FIELD(hasSubLinks);
	COMPARE_SCALAR_FIELD(hasDistinctOn);
	COMPARE_SCALAR_FIELD(hasRecursive);
	COMPARE_SCALAR_FIELD(hasModifyingCTE);
	COMPARE_SCALAR_FIELD(hasForUpdate);
	COMPARE_SCALAR_FIELD(hasRowSecurity);
	COMPARE_NODE_FIELD(cteList);
	COMPARE_NODE_FIELD(rtable);
	COMPARE_NODE_FIELD(jointree);
	COMPARE_NODE_FIELD(targetList);
	COMPARE_SCALAR_FIELD(override);
	COMPARE_NODE_FIELD(onConflict);
	COMPARE_NODE_FIELD(returningList);
	COMPARE_NODE_FIELD(groupClause);
	COMPARE_NODE_FIELD(groupingSets);
	COMPARE_NODE_FIELD(havingQual);
	COMPARE_NODE_FIELD(windowClause);
	COMPARE_NODE_FIELD(distinctClause);
	COMPARE_NODE_FIELD(sortClause);
	COMPARE_NODE_FIELD(limitOffset);
	COMPARE_NODE_FIELD(limitCount);
	COMPARE_NODE_FIELD(rowMarks);
	COMPARE_NODE_FIELD(setOperations);
	COMPARE_NODE_FIELD(constraintDeps);
	COMPARE_NODE_FIELD(withCheckOptions);
	COMPARE_LOCATION_FIELD(stmt_location);
	COMPARE_LOCATION_FIELD(stmt_len);

	return true;
}

static bool
_equalRawStmt(const RawStmt *a, const RawStmt *b)
{
	COMPARE_NODE_FIELD(stmt);
	COMPARE_LOCATION_FIELD(stmt_location);
	COMPARE_LOCATION_FIELD(stmt_len);

	return true;
}

static bool
_equalInsertStmt(const InsertStmt *a, const InsertStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(cols);
	COMPARE_NODE_FIELD(selectStmt);
	COMPARE_NODE_FIELD(onConflictClause);
	COMPARE_NODE_FIELD(returningList);
	COMPARE_NODE_FIELD(withClause);
	COMPARE_SCALAR_FIELD(override);

	return true;
}

static bool
_equalDeleteStmt(const DeleteStmt *a, const DeleteStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(usingClause);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_NODE_FIELD(returningList);
	COMPARE_NODE_FIELD(withClause);

	return true;
}

static bool
_equalUpdateStmt(const UpdateStmt *a, const UpdateStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(targetList);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_NODE_FIELD(fromClause);
	COMPARE_NODE_FIELD(returningList);
	COMPARE_NODE_FIELD(withClause);

	return true;
}

static bool
_equalSelectStmt(const SelectStmt *a, const SelectStmt *b)
{
	COMPARE_NODE_FIELD(distinctClause);
	COMPARE_NODE_FIELD(intoClause);
	COMPARE_NODE_FIELD(targetList);
	COMPARE_NODE_FIELD(fromClause);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_NODE_FIELD(groupClause);
	COMPARE_NODE_FIELD(havingClause);
	COMPARE_NODE_FIELD(windowClause);
	COMPARE_NODE_FIELD(valuesLists);
	COMPARE_NODE_FIELD(sortClause);
	COMPARE_NODE_FIELD(limitOffset);
	COMPARE_NODE_FIELD(limitCount);
	COMPARE_NODE_FIELD(lockingClause);
	COMPARE_NODE_FIELD(withClause);
	COMPARE_SCALAR_FIELD(op);
	COMPARE_SCALAR_FIELD(all);
	COMPARE_NODE_FIELD(larg);
	COMPARE_NODE_FIELD(rarg);

	return true;
}

static bool
_equalSetOperationStmt(const SetOperationStmt *a, const SetOperationStmt *b)
{
	COMPARE_SCALAR_FIELD(op);
	COMPARE_SCALAR_FIELD(all);
	COMPARE_NODE_FIELD(larg);
	COMPARE_NODE_FIELD(rarg);
	COMPARE_NODE_FIELD(colTypes);
	COMPARE_NODE_FIELD(colTypmods);
	COMPARE_NODE_FIELD(colCollations);
	COMPARE_NODE_FIELD(groupClauses);

	return true;
}

static bool
_equalAlterTableStmt(const AlterTableStmt *a, const AlterTableStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(cmds);
	COMPARE_SCALAR_FIELD(relkind);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalAlterTableCmd(const AlterTableCmd *a, const AlterTableCmd *b)
{
	COMPARE_SCALAR_FIELD(subtype);
	COMPARE_STRING_FIELD(name);
	COMPARE_SCALAR_FIELD(num);
	COMPARE_NODE_FIELD(newowner);
	COMPARE_NODE_FIELD(def);
	COMPARE_SCALAR_FIELD(behavior);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalAlterCollationStmt(const AlterCollationStmt *a, const AlterCollationStmt *b)
{
	COMPARE_NODE_FIELD(collname);

	return true;
}

static bool
_equalAlterDomainStmt(const AlterDomainStmt *a, const AlterDomainStmt *b)
{
	COMPARE_SCALAR_FIELD(subtype);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(def);
	COMPARE_SCALAR_FIELD(behavior);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalGrantStmt(const GrantStmt *a, const GrantStmt *b)
{
	COMPARE_SCALAR_FIELD(is_grant);
	COMPARE_SCALAR_FIELD(targtype);
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(objects);
	COMPARE_NODE_FIELD(privileges);
	COMPARE_NODE_FIELD(grantees);
	COMPARE_SCALAR_FIELD(grant_option);
	COMPARE_SCALAR_FIELD(behavior);

	return true;
}

static bool
_equalObjectWithArgs(const ObjectWithArgs *a, const ObjectWithArgs *b)
{
	COMPARE_NODE_FIELD(objname);
	COMPARE_NODE_FIELD(objargs);
	COMPARE_SCALAR_FIELD(args_unspecified);

	return true;
}
int main (int argc, char *argv []) {
    int size;
    int rank;
    const int VERY_LARGE_INT = 999999;
    const int ROOT = 0;
    int tag = 1234;
    MPI_Init (& argc, & argv);
    MPI_Comm_size (MPI_COMM_WORLD, & size);
    MPI_Comm_rank (MPI_COMM_WORLD, & rank);
    int count = N / size;
    int *localArray = (int *) malloc (count * sizeof (int));
    int localMin;
    int globalMin;
    if (rank == ROOT) {
        for (int i = 0; i < N; i++) {
            A[i] = rand () % 10;
        }
        for (int i = 0; i < count; i++)
            localArray[i] = A[i];
        for (int dest = 1; dest < size; ++dest) {
            MPI_Send (& A [dest * count], count, MPI_INT, dest, tag, MPI_COMM_WORLD);
            printf ("P0 sent a %d elements to P%d.\n", count, dest);
        }
        localMin = VERY_LARGE_INT;
        for (int source = 1; source < size; source++) {
            MPI_Recv (localArray, count, MPI_INT, source, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf ("Received results from task %d\n", source);
        }
    }
    else {
        MPI_Recv (localArray, count, MPI_INT, ROOT, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        MPI_Send (localArray, count, MPI_INT, ROOT, 2, MPI_COMM_WORLD);
    }
    MPI_Finalize ();
    return 0;
}

int crc32 (char *addr, int num, int crc) {
    int i;
    for (; num > 0; num--) {
        crc = crc ^ *addr++;
        for (i = 0; i < 8; i++) {
            if (crc & 1)
                crc = (crc >> 1) ^ poly;
            else
                crc >>= 1;
        }
    }
    return (crc);
}


static bool
_equalAccessPriv(const AccessPriv *a, const AccessPriv *b)
{
	COMPARE_STRING_FIELD(priv_name);
	COMPARE_NODE_FIELD(cols);

	return true;
}

static bool
_equalGrantRoleStmt(const GrantRoleStmt *a, const GrantRoleStmt *b)
{
	COMPARE_NODE_FIELD(granted_roles);
	COMPARE_NODE_FIELD(grantee_roles);
	COMPARE_SCALAR_FIELD(is_grant);
	COMPARE_SCALAR_FIELD(admin_opt);
	COMPARE_NODE_FIELD(grantor);
	COMPARE_SCALAR_FIELD(behavior);

	return true;
}

static bool
_equalAlterDefaultPrivilegesStmt(const AlterDefaultPrivilegesStmt *a, const AlterDefaultPrivilegesStmt *b)
{
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(action);

	return true;
}

static bool
_equalDeclareCursorStmt(const DeclareCursorStmt *a, const DeclareCursorStmt *b)
{
	COMPARE_STRING_FIELD(portalname);
	COMPARE_SCALAR_FIELD(options);
	COMPARE_NODE_FIELD(query);

	return true;
}

static bool
_equalClosePortalStmt(const ClosePortalStmt *a, const ClosePortalStmt *b)
{
	COMPARE_STRING_FIELD(portalname);

	return true;
}

static bool
_equalCallStmt(const CallStmt *a, const CallStmt *b)
{
	COMPARE_NODE_FIELD(funccall);
	COMPARE_NODE_FIELD(funcexpr);

	return true;
}

static bool
_equalClusterStmt(const ClusterStmt *a, const ClusterStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_STRING_FIELD(indexname);
	COMPARE_SCALAR_FIELD(options);

	return true;
}

static bool
_equalCopyStmt(const CopyStmt *a, const CopyStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(query);
	COMPARE_NODE_FIELD(attlist);
	COMPARE_SCALAR_FIELD(is_from);
	COMPARE_SCALAR_FIELD(is_program);
	COMPARE_STRING_FIELD(filename);
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(whereClause);

	return true;
}

static bool
_equalCreateStmt(const CreateStmt *a, const CreateStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(tableElts);
	COMPARE_NODE_FIELD(inhRelations);
	COMPARE_NODE_FIELD(partbound);
	COMPARE_NODE_FIELD(partspec);
	COMPARE_NODE_FIELD(ofTypename);
	COMPARE_NODE_FIELD(constraints);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(oncommit);
	COMPARE_STRING_FIELD(tablespacename);
	COMPARE_STRING_FIELD(accessMethod);
	COMPARE_SCALAR_FIELD(if_not_exists);

	return true;
}

static bool
_equalTableLikeClause(const TableLikeClause *a, const TableLikeClause *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_SCALAR_FIELD(options);

	return true;
}

static bool
_equalDefineStmt(const DefineStmt *a, const DefineStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_SCALAR_FIELD(oldstyle);
	COMPARE_NODE_FIELD(defnames);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(definition);
	COMPARE_SCALAR_FIELD(if_not_exists);
	COMPARE_SCALAR_FIELD(replace);

	return true;
}

static bool
_equalDropStmt(const DropStmt *a, const DropStmt *b)
{
	COMPARE_NODE_FIELD(objects);
	COMPARE_SCALAR_FIELD(removeType);
	COMPARE_SCALAR_FIELD(behavior);
	COMPARE_SCALAR_FIELD(missing_ok);
	COMPARE_SCALAR_FIELD(concurrent);

	return true;
}

static bool
_equalTruncateStmt(const TruncateStmt *a, const TruncateStmt *b)
{
	COMPARE_NODE_FIELD(relations);
	COMPARE_SCALAR_FIELD(restart_seqs);
	COMPARE_SCALAR_FIELD(behavior);

	return true;
}
int main (void) {
    int i;
    printf ("Enter a number: ");
    scanf ("%d", & i);
    if (isdigit (i)) {
        printf ("It is a digit.");
    }
    else {
        if (test_prime (i))
            printf ("Prime.\n");
        else
            printf ("Not prime.\n");
    }
    return 0;
}


static bool
_equalCommentStmt(const CommentStmt *a, const CommentStmt *b)
{
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(object);
	COMPARE_STRING_FIELD(comment);

	return true;
}

static bool
_equalSecLabelStmt(const SecLabelStmt *a, const SecLabelStmt *b)
{
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(object);
	COMPARE_STRING_FIELD(provider);
	COMPARE_STRING_FIELD(label);

	return true;
}

static bool
_equalFetchStmt(const FetchStmt *a, const FetchStmt *b)
{
	COMPARE_SCALAR_FIELD(direction);
	COMPARE_SCALAR_FIELD(howMany);
	COMPARE_STRING_FIELD(portalname);
	COMPARE_SCALAR_FIELD(ismove);

	return true;
}

static bool
_equalIndexStmt(const IndexStmt *a, const IndexStmt *b)
{
	COMPARE_STRING_FIELD(idxname);
	COMPARE_NODE_FIELD(relation);
	COMPARE_STRING_FIELD(accessMethod);
	COMPARE_STRING_FIELD(tableSpace);
	COMPARE_NODE_FIELD(indexParams);
	COMPARE_NODE_FIELD(indexIncludingParams);
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_NODE_FIELD(excludeOpNames);
	COMPARE_STRING_FIELD(idxcomment);
	COMPARE_SCALAR_FIELD(indexOid);
	COMPARE_SCALAR_FIELD(oldNode);
	COMPARE_SCALAR_FIELD(unique);
	COMPARE_SCALAR_FIELD(primary);
	COMPARE_SCALAR_FIELD(isconstraint);
	COMPARE_SCALAR_FIELD(deferrable);
	COMPARE_SCALAR_FIELD(initdeferred);
	COMPARE_SCALAR_FIELD(transformed);
	COMPARE_SCALAR_FIELD(concurrent);
	COMPARE_SCALAR_FIELD(if_not_exists);
	COMPARE_SCALAR_FIELD(reset_default_tblspc);

	return true;
}

static bool
_equalCreateStatsStmt(const CreateStatsStmt *a, const CreateStatsStmt *b)
{
	COMPARE_NODE_FIELD(defnames);
	COMPARE_NODE_FIELD(stat_types);
	COMPARE_NODE_FIELD(exprs);
	COMPARE_NODE_FIELD(relations);
	COMPARE_STRING_FIELD(stxcomment);
	COMPARE_SCALAR_FIELD(if_not_exists);

	return true;
}

static bool
_equalCreateFunctionStmt(const CreateFunctionStmt *a, const CreateFunctionStmt *b)
{
	COMPARE_SCALAR_FIELD(is_procedure);
	COMPARE_SCALAR_FIELD(replace);
	COMPARE_NODE_FIELD(funcname);
	COMPARE_NODE_FIELD(parameters);
	COMPARE_NODE_FIELD(returnType);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalFunctionParameter(const FunctionParameter *a, const FunctionParameter *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(argType);
	COMPARE_SCALAR_FIELD(mode);
	COMPARE_NODE_FIELD(defexpr);

	return true;
}

static bool
_equalAlterFunctionStmt(const AlterFunctionStmt *a, const AlterFunctionStmt *b)
{
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(func);
	COMPARE_NODE_FIELD(actions);

	return true;
}

static bool
_equalDoStmt(const DoStmt *a, const DoStmt *b)
{
	COMPARE_NODE_FIELD(args);

	return true;
}
int main () {
    char passcode [] = "ZZZ";
    char input [50];
    int check;
    do {
        printf ("What is the password?\n");
        fgets (input, sizeof (input), stdin);
        check = strcmp (passcode, input);
    }
    while (check != 0);
    printf ("You crack the pass code!");
    return 0;
}

int main () {
    struct timespec start, finish;
    clock_gettime (CLOCK_REALTIME, & start);
    clock_gettime (CLOCK_REALTIME, & finish);
    long seconds = finish.tv_sec - start.tv_sec;
    long ns = finish.tv_nsec - start.tv_nsec;
    if (start.tv_nsec > finish.tv_nsec) {
        --seconds;
        ns += 1000000000;
    }
    printf ("seconds without ns: %ld\n", seconds);
    printf ("nanoseconds: %ld\n", ns);
    printf ("total seconds: %e\n", (double) seconds + (double) ns / (double) 1000000000);
}


static bool
_equalRenameStmt(const RenameStmt *a, const RenameStmt *b)
{
	COMPARE_SCALAR_FIELD(renameType);
	COMPARE_SCALAR_FIELD(relationType);
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(object);
	COMPARE_STRING_FIELD(subname);
	COMPARE_STRING_FIELD(newname);
	COMPARE_SCALAR_FIELD(behavior);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalAlterObjectDependsStmt(const AlterObjectDependsStmt *a, const AlterObjectDependsStmt *b)
{
	COMPARE_SCALAR_FIELD(objectType);
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(object);
	COMPARE_NODE_FIELD(extname);

	return true;
}

static bool
_equalAlterObjectSchemaStmt(const AlterObjectSchemaStmt *a, const AlterObjectSchemaStmt *b)
{
	COMPARE_SCALAR_FIELD(objectType);
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(object);
	COMPARE_STRING_FIELD(newschema);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalAlterOwnerStmt(const AlterOwnerStmt *a, const AlterOwnerStmt *b)
{
	COMPARE_SCALAR_FIELD(objectType);
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(object);
	COMPARE_NODE_FIELD(newowner);

	return true;
}

static bool
_equalAlterOperatorStmt(const AlterOperatorStmt *a, const AlterOperatorStmt *b)
{
	COMPARE_NODE_FIELD(opername);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalRuleStmt(const RuleStmt *a, const RuleStmt *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_STRING_FIELD(rulename);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_SCALAR_FIELD(event);
	COMPARE_SCALAR_FIELD(instead);
	COMPARE_NODE_FIELD(actions);
	COMPARE_SCALAR_FIELD(replace);

	return true;
}

static bool
_equalNotifyStmt(const NotifyStmt *a, const NotifyStmt *b)
{
	COMPARE_STRING_FIELD(conditionname);
	COMPARE_STRING_FIELD(payload);

	return true;
}

static bool
_equalListenStmt(const ListenStmt *a, const ListenStmt *b)
{
	COMPARE_STRING_FIELD(conditionname);

	return true;
}

static bool
_equalUnlistenStmt(const UnlistenStmt *a, const UnlistenStmt *b)
{
	COMPARE_STRING_FIELD(conditionname);

	return true;
}
int main () {
    int n1, n2, sum, tmp, digit, dec_digits;
    printf ("Enter the lower limit: ");
    scanf ("%d", & n1);
    printf ("\nEnter the upper limit: ");
    scanf ("%d", & n2);
    while (n1 <= n2) {
        sum = 0;
        dec_digits = decimal_digits (n1);
        tmp = n1;
        while (tmp != 0) {
            digit = tmp % 10;
            sum += (int) uipow ((uint32_t) digit, (uint32_t) dec_digits);
            tmp = tmp / 10;
        }
        if (sum == n1) {
            printf ("%d\n", n1);
        }
        n1++;
    }
    exit (EXIT_SUCCESS);
}

int main () {
    int k;
    struct sigdeath_notify_info death;
    daft_thread_accounting_info_init (& g_thread_accounting);
    register_signal_handlers ();
    for (k = 0; k < 200; ++k) {
        start_daft_thread (someone_please_fix_me, (void *) k);
    }
    while (read (g_thread_accounting.monitor_pipe[0], &death, sizeof (death)) == sizeof (death)) {
        struct daft_thread_t *info = find_thread_by_tid (death.tid);
        if (info == NULL) {
            fprintf (stderr, "*** thread_id %u not found\n", death.tid);
            continue;
        }
        fprintf (stderr, "Thread %u (%d) died of %d, restarting.\n", death.tid, (int) info -> start_routine_arg, death.signum);
        restart_daft_thread (info);
    }
    fprintf (stderr, "Shouldn't get here.\n");
    return 0;
}


static bool
_equalTransactionStmt(const TransactionStmt *a, const TransactionStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(options);
	COMPARE_STRING_FIELD(savepoint_name);
	COMPARE_STRING_FIELD(gid);
	COMPARE_SCALAR_FIELD(chain);

	return true;
}

static bool
_equalCompositeTypeStmt(const CompositeTypeStmt *a, const CompositeTypeStmt *b)
{
	COMPARE_NODE_FIELD(typevar);
	COMPARE_NODE_FIELD(coldeflist);

	return true;
}

static bool
_equalCreateEnumStmt(const CreateEnumStmt *a, const CreateEnumStmt *b)
{
	COMPARE_NODE_FIELD(typeName);
	COMPARE_NODE_FIELD(vals);

	return true;
}

static bool
_equalCreateRangeStmt(const CreateRangeStmt *a, const CreateRangeStmt *b)
{
	COMPARE_NODE_FIELD(typeName);
	COMPARE_NODE_FIELD(params);

	return true;
}
int foo () {
    char *p = NULL;
    char *q = NULL;
    int ret = 0;
    if (NULL == (p = malloc (BUFSIZ))) {
        ret = ERROR_CODE;
        goto error;
    }
    if (NULL == (q = malloc (BUFSIZ))) {
        ret = ERROR_CODE;
        goto error;
    }
error :
    free (p);
    free (q);
    return ret;
}


static bool
_equalAlterEnumStmt(const AlterEnumStmt *a, const AlterEnumStmt *b)
{
	COMPARE_NODE_FIELD(typeName);
	COMPARE_STRING_FIELD(oldVal);
	COMPARE_STRING_FIELD(newVal);
	COMPARE_STRING_FIELD(newValNeighbor);
	COMPARE_SCALAR_FIELD(newValIsAfter);
	COMPARE_SCALAR_FIELD(skipIfNewValExists);

	return true;
}

static bool
_equalViewStmt(const ViewStmt *a, const ViewStmt *b)
{
	COMPARE_NODE_FIELD(view);
	COMPARE_NODE_FIELD(aliases);
	COMPARE_NODE_FIELD(query);
	COMPARE_SCALAR_FIELD(replace);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(withCheckOption);

	return true;
}

static bool
_equalLoadStmt(const LoadStmt *a, const LoadStmt *b)
{
	COMPARE_STRING_FIELD(filename);

	return true;
}

static bool
_equalCreateDomainStmt(const CreateDomainStmt *a, const CreateDomainStmt *b)
{
	COMPARE_NODE_FIELD(domainname);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_NODE_FIELD(collClause);
	COMPARE_NODE_FIELD(constraints);

	return true;
}

static bool
_equalCreateOpClassStmt(const CreateOpClassStmt *a, const CreateOpClassStmt *b)
{
	COMPARE_NODE_FIELD(opclassname);
	COMPARE_NODE_FIELD(opfamilyname);
	COMPARE_STRING_FIELD(amname);
	COMPARE_NODE_FIELD(datatype);
	COMPARE_NODE_FIELD(items);
	COMPARE_SCALAR_FIELD(isDefault);

	return true;
}

static bool
_equalCreateOpClassItem(const CreateOpClassItem *a, const CreateOpClassItem *b)
{
	COMPARE_SCALAR_FIELD(itemtype);
	COMPARE_NODE_FIELD(name);
	COMPARE_SCALAR_FIELD(number);
	COMPARE_NODE_FIELD(order_family);
	COMPARE_NODE_FIELD(class_args);
	COMPARE_NODE_FIELD(storedtype);

	return true;
}
int main (void) {
    int choice;
    char name [100];
    printf ("Enter name: ");
    scanf ("%99s", name);
    clear_stream ();
    printf ("Play a game, %s (y/n)? ", name);
    choice = get_single_char ();
    if (choice == 'y') {
        printf ("Press ENTER to continue:");
        get_single_char ();
    }
    else {
        puts ("That was uninspiring!");
    }
    puts ("bye");
    return 0;
}


static bool
_equalCreateOpFamilyStmt(const CreateOpFamilyStmt *a, const CreateOpFamilyStmt *b)
{
	COMPARE_NODE_FIELD(opfamilyname);
	COMPARE_STRING_FIELD(amname);

	return true;
}

static bool
_equalAlterOpFamilyStmt(const AlterOpFamilyStmt *a, const AlterOpFamilyStmt *b)
{
	COMPARE_NODE_FIELD(opfamilyname);
	COMPARE_STRING_FIELD(amname);
	COMPARE_SCALAR_FIELD(isDrop);
	COMPARE_NODE_FIELD(items);

	return true;
}
int main () {
    char *hexstring = "deadbeef10203040b00b1e50";
    int i;
    unsigned int bytearray [12];
    uint8_t str_len = strlen (hexstring);
    for (i = 0; i < (str_len / 2); i++) {
        sscanf (hexstring + 2 * i, "%02x", & bytearray [i]);
        printf ("bytearray %d: %02x\n", i, bytearray [i]);
    }
    return 0;
}


static bool
_equalCreatedbStmt(const CreatedbStmt *a, const CreatedbStmt *b)
{
	COMPARE_STRING_FIELD(dbname);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterDatabaseStmt(const AlterDatabaseStmt *a, const AlterDatabaseStmt *b)
{
	COMPARE_STRING_FIELD(dbname);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterDatabaseSetStmt(const AlterDatabaseSetStmt *a, const AlterDatabaseSetStmt *b)
{
	COMPARE_STRING_FIELD(dbname);
	COMPARE_NODE_FIELD(setstmt);

	return true;
}

static bool
_equalDropdbStmt(const DropdbStmt *a, const DropdbStmt *b)
{
	COMPARE_STRING_FIELD(dbname);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalVacuumStmt(const VacuumStmt *a, const VacuumStmt *b)
{
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(rels);
	COMPARE_SCALAR_FIELD(is_vacuumcmd);

	return true;
}

static bool
_equalVacuumRelation(const VacuumRelation *a, const VacuumRelation *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_SCALAR_FIELD(oid);
	COMPARE_NODE_FIELD(va_cols);

	return true;
}

static bool
_equalExplainStmt(const ExplainStmt *a, const ExplainStmt *b)
{
	COMPARE_NODE_FIELD(query);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalCreateTableAsStmt(const CreateTableAsStmt *a, const CreateTableAsStmt *b)
{
	COMPARE_NODE_FIELD(query);
	COMPARE_NODE_FIELD(into);
	COMPARE_SCALAR_FIELD(relkind);
	COMPARE_SCALAR_FIELD(is_select_into);
	COMPARE_SCALAR_FIELD(if_not_exists);

	return true;
}

static bool
_equalRefreshMatViewStmt(const RefreshMatViewStmt *a, const RefreshMatViewStmt *b)
{
	COMPARE_SCALAR_FIELD(concurrent);
	COMPARE_SCALAR_FIELD(skipData);
	COMPARE_NODE_FIELD(relation);

	return true;
}

static bool
_equalReplicaIdentityStmt(const ReplicaIdentityStmt *a, const ReplicaIdentityStmt *b)
{
	COMPARE_SCALAR_FIELD(identity_type);
	COMPARE_STRING_FIELD(name);

	return true;
}

static bool
_equalAlterSystemStmt(const AlterSystemStmt *a, const AlterSystemStmt *b)
{
	COMPARE_NODE_FIELD(setstmt);

	return true;
}


static bool
_equalCreateSeqStmt(const CreateSeqStmt *a, const CreateSeqStmt *b)
{
	COMPARE_NODE_FIELD(sequence);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(ownerId);
	COMPARE_SCALAR_FIELD(for_identity);
	COMPARE_SCALAR_FIELD(if_not_exists);

	return true;
}

static bool
_equalAlterSeqStmt(const AlterSeqStmt *a, const AlterSeqStmt *b)
{
	COMPARE_NODE_FIELD(sequence);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(for_identity);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalVariableSetStmt(const VariableSetStmt *a, const VariableSetStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(args);
	COMPARE_SCALAR_FIELD(is_local);

	return true;
}

static bool
_equalVariableShowStmt(const VariableShowStmt *a, const VariableShowStmt *b)
{
	COMPARE_STRING_FIELD(name);

	return true;
}

static bool
_equalDiscardStmt(const DiscardStmt *a, const DiscardStmt *b)
{
	COMPARE_SCALAR_FIELD(target);

	return true;
}
int main (void) {
    int boundary, choice, isq, ssq;
    while (1) {
        printf ("Enter an integer: ");
        scanf ("%d", & boundary);
        ssq = 0;
        for (isq = 1; isq <= boundary; isq++) {
            ssq = ssq + (isq * isq);
        }
        printf ("The sum of the squares of integers from 0 to %d is %d\n", boundary, ssq);
        printf ("Would you like to go again? (1 for yes, 0 for no): ");
        scanf ("%d", & choice);
        if (choice == 0)
            break;
    }
    return 0;
}


static bool
_equalCreateTableSpaceStmt(const CreateTableSpaceStmt *a, const CreateTableSpaceStmt *b)
{
	COMPARE_STRING_FIELD(tablespacename);
	COMPARE_NODE_FIELD(owner);
	COMPARE_STRING_FIELD(location);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalDropTableSpaceStmt(const DropTableSpaceStmt *a, const DropTableSpaceStmt *b)
{
	COMPARE_STRING_FIELD(tablespacename);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalAlterTableSpaceOptionsStmt(const AlterTableSpaceOptionsStmt *a,
								 const AlterTableSpaceOptionsStmt *b)
{
	COMPARE_STRING_FIELD(tablespacename);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(isReset);

	return true;
}
int main () {
    int total = 0;
    double acc = 0, val;
    for (;;) {
        fputs ("Value: ", stdout);
        fflush (stdout);
        errno = 0;
        int res = fscanf (stdin, "%lf", &val);
        if (res == EOF) {
            if (errno == 0) {
                fprintf (stdout, "Done! You entered %d values averaging %f.\n", total, acc / total);
            }
            else {
                fputs ("There was an error, aborting!\n", stdout);
            }
            break;
        }
        else if (res == 0) {
            fputs ("Sorry, I did not understand. Try again.\n", stdout);
            clearerr (stdin);
            for (int r = 0; r != EOF && r != '\n'; r = fgetc (stdin)) {
            }
        }
        else {
            acc += val;
            ++total;
        }
    }
}


static bool
_equalAlterTableMoveAllStmt(const AlterTableMoveAllStmt *a,
							const AlterTableMoveAllStmt *b)
{
	COMPARE_STRING_FIELD(orig_tablespacename);
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(roles);
	COMPARE_STRING_FIELD(new_tablespacename);
	COMPARE_SCALAR_FIELD(nowait);

	return true;
}

static bool
_equalCreateExtensionStmt(const CreateExtensionStmt *a, const CreateExtensionStmt *b)
{
	COMPARE_STRING_FIELD(extname);
	COMPARE_SCALAR_FIELD(if_not_exists);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterExtensionStmt(const AlterExtensionStmt *a, const AlterExtensionStmt *b)
{
	COMPARE_STRING_FIELD(extname);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterExtensionContentsStmt(const AlterExtensionContentsStmt *a, const AlterExtensionContentsStmt *b)
{
	COMPARE_STRING_FIELD(extname);
	COMPARE_SCALAR_FIELD(action);
	COMPARE_SCALAR_FIELD(objtype);
	COMPARE_NODE_FIELD(object);

	return true;
}

static bool
_equalCreateFdwStmt(const CreateFdwStmt *a, const CreateFdwStmt *b)
{
	COMPARE_STRING_FIELD(fdwname);
	COMPARE_NODE_FIELD(func_options);
	COMPARE_NODE_FIELD(options);

	return true;
}
int main (int argc, char **argv) {
    int buf_size = 0;
    int buf_used = 0;
    char *buf = NULL;
    char *tmp = NULL;
    char c;
    int i = 0;
    while ((c = getchar ()) != EOF) {
        if (buf_used == buf_size) {
            buf_size += 20;
            tmp = realloc (buf, buf_size);
            if (!tmp)
                fatal_error ();
            buf = tmp;
        }
        buf[buf_used] = c;
        ++buf_used;
    }
    puts ("\n\n*** Dump of stdin ***\n");
    for (i = 0; i < buf_used; ++i) {
        putchar (buf [i]);
    }
    free (buf);
    return 0;
}


static bool
_equalAlterFdwStmt(const AlterFdwStmt *a, const AlterFdwStmt *b)
{
	COMPARE_STRING_FIELD(fdwname);
	COMPARE_NODE_FIELD(func_options);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalCreateForeignServerStmt(const CreateForeignServerStmt *a, const CreateForeignServerStmt *b)
{
	COMPARE_STRING_FIELD(servername);
	COMPARE_STRING_FIELD(servertype);
	COMPARE_STRING_FIELD(version);
	COMPARE_STRING_FIELD(fdwname);
	COMPARE_SCALAR_FIELD(if_not_exists);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterForeignServerStmt(const AlterForeignServerStmt *a, const AlterForeignServerStmt *b)
{
	COMPARE_STRING_FIELD(servername);
	COMPARE_STRING_FIELD(version);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(has_version);

	return true;
}

static bool
_equalCreateUserMappingStmt(const CreateUserMappingStmt *a, const CreateUserMappingStmt *b)
{
	COMPARE_NODE_FIELD(user);
	COMPARE_STRING_FIELD(servername);
	COMPARE_SCALAR_FIELD(if_not_exists);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterUserMappingStmt(const AlterUserMappingStmt *a, const AlterUserMappingStmt *b)
{
	COMPARE_NODE_FIELD(user);
	COMPARE_STRING_FIELD(servername);
	COMPARE_NODE_FIELD(options);

	return true;
}
int main (void) {
    int x [10];
    int i, n, first, second;
    printf ("Input the size of array :");
    if (scanf ("%d", &n) != 1 || n < 0 || n > 10) {
        printf ("invalid input\n");
        return 1;
    }
    if (n <= 0) {
        first = second = 0;
    }
    else {
        printf ("Input %d elements in the array:\n", n);
        for (i = 0; i < n; i++) {
            printf ("x[%d]: ", i);
            if (scanf ("%d", &x[i]) != 1) {
                printf ("invalid input\n");
                return 1;
            }
        }
        first = second = x[0];
        for (i = 1; i < n; ++i) {
            if (first < x[i]) {
                second = first;
                first = x[i];
            }
            else if (x[i] > second && x[i] != first) {
                second = x[i];
            }
        }
    }
    if (second == first)
        printf ("There is no second largest element\n");
    else
        printf ("\nThe Second largest element in the array is: %d\n", second);
    return 0;
}


static bool
_equalDropUserMappingStmt(const DropUserMappingStmt *a, const DropUserMappingStmt *b)
{
	COMPARE_NODE_FIELD(user);
	COMPARE_STRING_FIELD(servername);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalCreateForeignTableStmt(const CreateForeignTableStmt *a, const CreateForeignTableStmt *b)
{
	if (!_equalCreateStmt(&a->base, &b->base))
		return false;

	COMPARE_STRING_FIELD(servername);
	COMPARE_NODE_FIELD(options);

	return true;
}
int foo () {
    char *p = NULL;
    char *q = NULL;
    int ret = 0;
    do {
        if (NULL == (p = malloc (BUFSIZ))) {
            ret = ERROR_CODE;
            break;
        }
        if (NULL == (q = malloc (BUFSIZ))) {
            ret = ERROR_CODE;
            break;
        }
    }
    while (0);
    free (p);
    free (q);
    return ret;
}


static bool
_equalImportForeignSchemaStmt(const ImportForeignSchemaStmt *a, const ImportForeignSchemaStmt *b)
{
	COMPARE_STRING_FIELD(server_name);
	COMPARE_STRING_FIELD(remote_schema);
	COMPARE_STRING_FIELD(local_schema);
	COMPARE_SCALAR_FIELD(list_type);
	COMPARE_NODE_FIELD(table_list);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalCreateTransformStmt(const CreateTransformStmt *a, const CreateTransformStmt *b)
{
	COMPARE_SCALAR_FIELD(replace);
	COMPARE_NODE_FIELD(type_name);
	COMPARE_STRING_FIELD(lang);
	COMPARE_NODE_FIELD(fromsql);
	COMPARE_NODE_FIELD(tosql);

	return true;
}

static bool
_equalCreateAmStmt(const CreateAmStmt *a, const CreateAmStmt *b)
{
	COMPARE_STRING_FIELD(amname);
	COMPARE_NODE_FIELD(handler_name);
	COMPARE_SCALAR_FIELD(amtype);

	return true;
}

static bool
_equalCreateTrigStmt(const CreateTrigStmt *a, const CreateTrigStmt *b)
{
	COMPARE_STRING_FIELD(trigname);
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(funcname);
	COMPARE_NODE_FIELD(args);
	COMPARE_SCALAR_FIELD(row);
	COMPARE_SCALAR_FIELD(timing);
	COMPARE_SCALAR_FIELD(events);
	COMPARE_NODE_FIELD(columns);
	COMPARE_NODE_FIELD(whenClause);
	COMPARE_SCALAR_FIELD(isconstraint);
	COMPARE_NODE_FIELD(transitionRels);
	COMPARE_SCALAR_FIELD(deferrable);
	COMPARE_SCALAR_FIELD(initdeferred);
	COMPARE_NODE_FIELD(constrrel);

	return true;
}

static bool
_equalCreateEventTrigStmt(const CreateEventTrigStmt *a, const CreateEventTrigStmt *b)
{
	COMPARE_STRING_FIELD(trigname);
	COMPARE_STRING_FIELD(eventname);
	COMPARE_NODE_FIELD(whenclause);
	COMPARE_NODE_FIELD(funcname);

	return true;
}

static bool
_equalAlterEventTrigStmt(const AlterEventTrigStmt *a, const AlterEventTrigStmt *b)
{
	COMPARE_STRING_FIELD(trigname);
	COMPARE_SCALAR_FIELD(tgenabled);

	return true;
}

static bool
_equalCreatePLangStmt(const CreatePLangStmt *a, const CreatePLangStmt *b)
{
	COMPARE_SCALAR_FIELD(replace);
	COMPARE_STRING_FIELD(plname);
	COMPARE_NODE_FIELD(plhandler);
	COMPARE_NODE_FIELD(plinline);
	COMPARE_NODE_FIELD(plvalidator);
	COMPARE_SCALAR_FIELD(pltrusted);

	return true;
}
uint64_t pack (float a, float b) {
    union converter ca = {
        .f = a
    };
    union converter cb = {
        .f = b
    };
    return ((uint64_t) cb.i << 32) + ca.i;
}


static bool
_equalCreateRoleStmt(const CreateRoleStmt *a, const CreateRoleStmt *b)
{
	COMPARE_SCALAR_FIELD(stmt_type);
	COMPARE_STRING_FIELD(role);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterRoleStmt(const AlterRoleStmt *a, const AlterRoleStmt *b)
{
	COMPARE_NODE_FIELD(role);
	COMPARE_NODE_FIELD(options);
	COMPARE_SCALAR_FIELD(action);

	return true;
}

static bool
_equalAlterRoleSetStmt(const AlterRoleSetStmt *a, const AlterRoleSetStmt *b)
{
	COMPARE_NODE_FIELD(role);
	COMPARE_STRING_FIELD(database);
	COMPARE_NODE_FIELD(setstmt);

	return true;
}

static bool
_equalDropRoleStmt(const DropRoleStmt *a, const DropRoleStmt *b)
{
	COMPARE_NODE_FIELD(roles);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalLockStmt(const LockStmt *a, const LockStmt *b)
{
	COMPARE_NODE_FIELD(relations);
	COMPARE_SCALAR_FIELD(mode);
	COMPARE_SCALAR_FIELD(nowait);

	return true;
}

static bool
_equalConstraintsSetStmt(const ConstraintsSetStmt *a, const ConstraintsSetStmt *b)
{
	COMPARE_NODE_FIELD(constraints);
	COMPARE_SCALAR_FIELD(deferred);

	return true;
}

static bool
_equalReindexStmt(const ReindexStmt *a, const ReindexStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(relation);
	COMPARE_STRING_FIELD(name);
	COMPARE_SCALAR_FIELD(options);
	COMPARE_SCALAR_FIELD(concurrent);

	return true;
}

static bool
_equalCreateSchemaStmt(const CreateSchemaStmt *a, const CreateSchemaStmt *b)
{
	COMPARE_STRING_FIELD(schemaname);
	COMPARE_NODE_FIELD(authrole);
	COMPARE_NODE_FIELD(schemaElts);
	COMPARE_SCALAR_FIELD(if_not_exists);

	return true;
}

static bool
_equalCreateConversionStmt(const CreateConversionStmt *a, const CreateConversionStmt *b)
{
	COMPARE_NODE_FIELD(conversion_name);
	COMPARE_STRING_FIELD(for_encoding_name);
	COMPARE_STRING_FIELD(to_encoding_name);
	COMPARE_NODE_FIELD(func_name);
	COMPARE_SCALAR_FIELD(def);

	return true;
}

static bool
_equalCreateCastStmt(const CreateCastStmt *a, const CreateCastStmt *b)
{
	COMPARE_NODE_FIELD(sourcetype);
	COMPARE_NODE_FIELD(targettype);
	COMPARE_NODE_FIELD(func);
	COMPARE_SCALAR_FIELD(context);
	COMPARE_SCALAR_FIELD(inout);

	return true;
}

static bool
_equalPrepareStmt(const PrepareStmt *a, const PrepareStmt *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(argtypes);
	COMPARE_NODE_FIELD(query);

	return true;
}

static bool
_equalExecuteStmt(const ExecuteStmt *a, const ExecuteStmt *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(params);

	return true;
}

static bool
_equalDeallocateStmt(const DeallocateStmt *a, const DeallocateStmt *b)
{
	COMPARE_STRING_FIELD(name);

	return true;
}

static bool
_equalDropOwnedStmt(const DropOwnedStmt *a, const DropOwnedStmt *b)
{
	COMPARE_NODE_FIELD(roles);
	COMPARE_SCALAR_FIELD(behavior);

	return true;
}

static bool
_equalReassignOwnedStmt(const ReassignOwnedStmt *a, const ReassignOwnedStmt *b)
{
	COMPARE_NODE_FIELD(roles);
	COMPARE_NODE_FIELD(newrole);

	return true;
}
int add (int x, int y) {
    int a, b;
    do {
        a = x & y;
        b = x ^ y;
        x = a << 1;
        y = b;
    }
    while (a);
    return b;
}


static bool
_equalAlterTSDictionaryStmt(const AlterTSDictionaryStmt *a, const AlterTSDictionaryStmt *b)
{
	COMPARE_NODE_FIELD(dictname);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterTSConfigurationStmt(const AlterTSConfigurationStmt *a,
							   const AlterTSConfigurationStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(cfgname);
	COMPARE_NODE_FIELD(tokentype);
	COMPARE_NODE_FIELD(dicts);
	COMPARE_SCALAR_FIELD(override);
	COMPARE_SCALAR_FIELD(replace);
	COMPARE_SCALAR_FIELD(missing_ok);

	return true;
}

static bool
_equalCreatePublicationStmt(const CreatePublicationStmt *a,
							const CreatePublicationStmt *b)
{
	COMPARE_STRING_FIELD(pubname);
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(tables);
	COMPARE_SCALAR_FIELD(for_all_tables);

	return true;
}

static bool
_equalAlterPublicationStmt(const AlterPublicationStmt *a,
						   const AlterPublicationStmt *b)
{
	COMPARE_STRING_FIELD(pubname);
	COMPARE_NODE_FIELD(options);
	COMPARE_NODE_FIELD(tables);
	COMPARE_SCALAR_FIELD(for_all_tables);
	COMPARE_SCALAR_FIELD(tableAction);

	return true;
}

static bool
_equalCreateSubscriptionStmt(const CreateSubscriptionStmt *a,
							 const CreateSubscriptionStmt *b)
{
	COMPARE_STRING_FIELD(subname);
	COMPARE_STRING_FIELD(conninfo);
	COMPARE_NODE_FIELD(publication);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalAlterSubscriptionStmt(const AlterSubscriptionStmt *a,
							const AlterSubscriptionStmt *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_STRING_FIELD(subname);
	COMPARE_STRING_FIELD(conninfo);
	COMPARE_NODE_FIELD(publication);
	COMPARE_NODE_FIELD(options);

	return true;
}

static bool
_equalDropSubscriptionStmt(const DropSubscriptionStmt *a,
						   const DropSubscriptionStmt *b)
{
	COMPARE_STRING_FIELD(subname);
	COMPARE_SCALAR_FIELD(missing_ok);
	COMPARE_SCALAR_FIELD(behavior);

	return true;
}

static bool
_equalCreatePolicyStmt(const CreatePolicyStmt *a, const CreatePolicyStmt *b)
{
	COMPARE_STRING_FIELD(policy_name);
	COMPARE_NODE_FIELD(table);
	COMPARE_STRING_FIELD(cmd_name);
	COMPARE_SCALAR_FIELD(permissive);
	COMPARE_NODE_FIELD(roles);
	COMPARE_NODE_FIELD(qual);
	COMPARE_NODE_FIELD(with_check);

	return true;
}

static bool
_equalAlterPolicyStmt(const AlterPolicyStmt *a, const AlterPolicyStmt *b)
{
	COMPARE_STRING_FIELD(policy_name);
	COMPARE_NODE_FIELD(table);
	COMPARE_NODE_FIELD(roles);
	COMPARE_NODE_FIELD(qual);
	COMPARE_NODE_FIELD(with_check);

	return true;
}

static bool
_equalAExpr(const A_Expr *a, const A_Expr *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(name);
	COMPARE_NODE_FIELD(lexpr);
	COMPARE_NODE_FIELD(rexpr);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalColumnRef(const ColumnRef *a, const ColumnRef *b)
{
	COMPARE_NODE_FIELD(fields);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalParamRef(const ParamRef *a, const ParamRef *b)
{
	COMPARE_SCALAR_FIELD(number);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalAConst(const A_Const *a, const A_Const *b)
{
	if (!equal(&a->val, &b->val))	/* hack for in-line Value field */
		return false;
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalFuncCall(const FuncCall *a, const FuncCall *b)
{
	COMPARE_NODE_FIELD(funcname);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(agg_order);
	COMPARE_NODE_FIELD(agg_filter);
	COMPARE_SCALAR_FIELD(agg_within_group);
	COMPARE_SCALAR_FIELD(agg_star);
	COMPARE_SCALAR_FIELD(agg_distinct);
	COMPARE_SCALAR_FIELD(func_variadic);
	COMPARE_NODE_FIELD(over);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalAStar(const A_Star *a, const A_Star *b)
{
	return true;
}

static bool
_equalAIndices(const A_Indices *a, const A_Indices *b)
{
	COMPARE_SCALAR_FIELD(is_slice);
	COMPARE_NODE_FIELD(lidx);
	COMPARE_NODE_FIELD(uidx);

	return true;
}

static bool
_equalA_Indirection(const A_Indirection *a, const A_Indirection *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(indirection);

	return true;
}

static bool
_equalA_ArrayExpr(const A_ArrayExpr *a, const A_ArrayExpr *b)
{
	COMPARE_NODE_FIELD(elements);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalResTarget(const ResTarget *a, const ResTarget *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(indirection);
	COMPARE_NODE_FIELD(val);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalMultiAssignRef(const MultiAssignRef *a, const MultiAssignRef *b)
{
	COMPARE_NODE_FIELD(source);
	COMPARE_SCALAR_FIELD(colno);
	COMPARE_SCALAR_FIELD(ncolumns);

	return true;
}

static bool
_equalTypeName(const TypeName *a, const TypeName *b)
{
	COMPARE_NODE_FIELD(names);
	COMPARE_SCALAR_FIELD(typeOid);
	COMPARE_SCALAR_FIELD(setof);
	COMPARE_SCALAR_FIELD(pct_type);
	COMPARE_NODE_FIELD(typmods);
	COMPARE_SCALAR_FIELD(typemod);
	COMPARE_NODE_FIELD(arrayBounds);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalTypeCast(const TypeCast *a, const TypeCast *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCollateClause(const CollateClause *a, const CollateClause *b)
{
	COMPARE_NODE_FIELD(arg);
	COMPARE_NODE_FIELD(collname);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalSortBy(const SortBy *a, const SortBy *b)
{
	COMPARE_NODE_FIELD(node);
	COMPARE_SCALAR_FIELD(sortby_dir);
	COMPARE_SCALAR_FIELD(sortby_nulls);
	COMPARE_NODE_FIELD(useOp);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalWindowDef(const WindowDef *a, const WindowDef *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_STRING_FIELD(refname);
	COMPARE_NODE_FIELD(partitionClause);
	COMPARE_NODE_FIELD(orderClause);
	COMPARE_SCALAR_FIELD(frameOptions);
	COMPARE_NODE_FIELD(startOffset);
	COMPARE_NODE_FIELD(endOffset);
	COMPARE_LOCATION_FIELD(location);

	return true;
}
int *calc (int x, int y, int z) {
    static int result [3] = {0, 0, 0};
    if (x > y && x > z) {
        result[0] = x;
        if (y < z) {
            result[2] = y;
            result[1] = z;
        }
        else {
            result[1] = y;
            result[2] = z;
        }
    }
    if (y > x && y > z) {
        result[0] = y;
        if (x < z) {
            result[2] = x;
            result[1] = z;
        }
        else {
            result[1] = x;
            result[2] = z;
        }
    }
    if (z > x && z > y) {
        result[0] = z;
        if (y < x) {
            result[2] = y;
            result[1] = x;
        }
        else {
            result[1] = y;
            result[2] = x;
        }
    }
    return result;
}


static bool
_equalRangeSubselect(const RangeSubselect *a, const RangeSubselect *b)
{
	COMPARE_SCALAR_FIELD(lateral);
	COMPARE_NODE_FIELD(subquery);
	COMPARE_NODE_FIELD(alias);

	return true;
}

static bool
_equalRangeFunction(const RangeFunction *a, const RangeFunction *b)
{
	COMPARE_SCALAR_FIELD(lateral);
	COMPARE_SCALAR_FIELD(ordinality);
	COMPARE_SCALAR_FIELD(is_rowsfrom);
	COMPARE_NODE_FIELD(functions);
	COMPARE_NODE_FIELD(alias);
	COMPARE_NODE_FIELD(coldeflist);

	return true;
}

static bool
_equalRangeTableSample(const RangeTableSample *a, const RangeTableSample *b)
{
	COMPARE_NODE_FIELD(relation);
	COMPARE_NODE_FIELD(method);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(repeatable);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalRangeTableFunc(const RangeTableFunc *a, const RangeTableFunc *b)
{
	COMPARE_SCALAR_FIELD(lateral);
	COMPARE_NODE_FIELD(docexpr);
	COMPARE_NODE_FIELD(rowexpr);
	COMPARE_NODE_FIELD(namespaces);
	COMPARE_NODE_FIELD(columns);
	COMPARE_NODE_FIELD(alias);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalRangeTableFuncCol(const RangeTableFuncCol *a, const RangeTableFuncCol *b)
{
	COMPARE_STRING_FIELD(colname);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_SCALAR_FIELD(for_ordinality);
	COMPARE_SCALAR_FIELD(is_not_null);
	COMPARE_NODE_FIELD(colexpr);
	COMPARE_NODE_FIELD(coldefexpr);
	COMPARE_LOCATION_FIELD(location);

	return true;
}


static bool
_equalIndexElem(const IndexElem *a, const IndexElem *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(expr);
	COMPARE_STRING_FIELD(indexcolname);
	COMPARE_NODE_FIELD(collation);
	COMPARE_NODE_FIELD(opclass);
	COMPARE_SCALAR_FIELD(ordering);
	COMPARE_SCALAR_FIELD(nulls_ordering);

	return true;
}

static bool
_equalColumnDef(const ColumnDef *a, const ColumnDef *b)
{
	COMPARE_STRING_FIELD(colname);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_SCALAR_FIELD(inhcount);
	COMPARE_SCALAR_FIELD(is_local);
	COMPARE_SCALAR_FIELD(is_not_null);
	COMPARE_SCALAR_FIELD(is_from_type);
	COMPARE_SCALAR_FIELD(storage);
	COMPARE_NODE_FIELD(raw_default);
	COMPARE_NODE_FIELD(cooked_default);
	COMPARE_SCALAR_FIELD(identity);
	COMPARE_NODE_FIELD(identitySequence);
	COMPARE_SCALAR_FIELD(generated);
	COMPARE_NODE_FIELD(collClause);
	COMPARE_SCALAR_FIELD(collOid);
	COMPARE_NODE_FIELD(constraints);
	COMPARE_NODE_FIELD(fdwoptions);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalConstraint(const Constraint *a, const Constraint *b)
{
	COMPARE_SCALAR_FIELD(contype);
	COMPARE_STRING_FIELD(conname);
	COMPARE_SCALAR_FIELD(deferrable);
	COMPARE_SCALAR_FIELD(initdeferred);
	COMPARE_LOCATION_FIELD(location);
	COMPARE_SCALAR_FIELD(is_no_inherit);
	COMPARE_NODE_FIELD(raw_expr);
	COMPARE_STRING_FIELD(cooked_expr);
	COMPARE_SCALAR_FIELD(generated_when);
	COMPARE_NODE_FIELD(keys);
	COMPARE_NODE_FIELD(including);
	COMPARE_NODE_FIELD(exclusions);
	COMPARE_NODE_FIELD(options);
	COMPARE_STRING_FIELD(indexname);
	COMPARE_STRING_FIELD(indexspace);
	COMPARE_SCALAR_FIELD(reset_default_tblspc);
	COMPARE_STRING_FIELD(access_method);
	COMPARE_NODE_FIELD(where_clause);
	COMPARE_NODE_FIELD(pktable);
	COMPARE_NODE_FIELD(fk_attrs);
	COMPARE_NODE_FIELD(pk_attrs);
	COMPARE_SCALAR_FIELD(fk_matchtype);
	COMPARE_SCALAR_FIELD(fk_upd_action);
	COMPARE_SCALAR_FIELD(fk_del_action);
	COMPARE_NODE_FIELD(old_conpfeqop);
	COMPARE_SCALAR_FIELD(old_pktable_oid);
	COMPARE_SCALAR_FIELD(skip_validation);
	COMPARE_SCALAR_FIELD(initially_valid);

	return true;
}

static bool
_equalDefElem(const DefElem *a, const DefElem *b)
{
	COMPARE_STRING_FIELD(defnamespace);
	COMPARE_STRING_FIELD(defname);
	COMPARE_NODE_FIELD(arg);
	COMPARE_SCALAR_FIELD(defaction);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalLockingClause(const LockingClause *a, const LockingClause *b)
{
	COMPARE_NODE_FIELD(lockedRels);
	COMPARE_SCALAR_FIELD(strength);
	COMPARE_SCALAR_FIELD(waitPolicy);

	return true;
}

static bool
_equalRangeTblEntry(const RangeTblEntry *a, const RangeTblEntry *b)
{
	COMPARE_SCALAR_FIELD(rtekind);
	COMPARE_SCALAR_FIELD(relid);
	COMPARE_SCALAR_FIELD(relkind);
	COMPARE_SCALAR_FIELD(rellockmode);
	COMPARE_NODE_FIELD(tablesample);
	COMPARE_NODE_FIELD(subquery);
	COMPARE_SCALAR_FIELD(security_barrier);
	COMPARE_SCALAR_FIELD(jointype);
	COMPARE_NODE_FIELD(joinaliasvars);
	COMPARE_NODE_FIELD(functions);
	COMPARE_SCALAR_FIELD(funcordinality);
	COMPARE_NODE_FIELD(tablefunc);
	COMPARE_NODE_FIELD(values_lists);
	COMPARE_STRING_FIELD(ctename);
	COMPARE_SCALAR_FIELD(ctelevelsup);
	COMPARE_SCALAR_FIELD(self_reference);
	COMPARE_NODE_FIELD(coltypes);
	COMPARE_NODE_FIELD(coltypmods);
	COMPARE_NODE_FIELD(colcollations);
	COMPARE_STRING_FIELD(enrname);
	COMPARE_SCALAR_FIELD(enrtuples);
	COMPARE_NODE_FIELD(alias);
	COMPARE_NODE_FIELD(eref);
	COMPARE_SCALAR_FIELD(lateral);
	COMPARE_SCALAR_FIELD(inh);
	COMPARE_SCALAR_FIELD(inFromCl);
	COMPARE_SCALAR_FIELD(requiredPerms);
	COMPARE_SCALAR_FIELD(checkAsUser);
	COMPARE_BITMAPSET_FIELD(selectedCols);
	COMPARE_BITMAPSET_FIELD(insertedCols);
	COMPARE_BITMAPSET_FIELD(updatedCols);
	COMPARE_BITMAPSET_FIELD(extraUpdatedCols);
	COMPARE_NODE_FIELD(securityQuals);

	return true;
}

static bool
_equalRangeTblFunction(const RangeTblFunction *a, const RangeTblFunction *b)
{
	COMPARE_NODE_FIELD(funcexpr);
	COMPARE_SCALAR_FIELD(funccolcount);
	COMPARE_NODE_FIELD(funccolnames);
	COMPARE_NODE_FIELD(funccoltypes);
	COMPARE_NODE_FIELD(funccoltypmods);
	COMPARE_NODE_FIELD(funccolcollations);
	COMPARE_BITMAPSET_FIELD(funcparams);

	return true;
}

static bool
_equalTableSampleClause(const TableSampleClause *a, const TableSampleClause *b)
{
	COMPARE_SCALAR_FIELD(tsmhandler);
	COMPARE_NODE_FIELD(args);
	COMPARE_NODE_FIELD(repeatable);

	return true;
}

static bool
_equalWithCheckOption(const WithCheckOption *a, const WithCheckOption *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_STRING_FIELD(relname);
	COMPARE_STRING_FIELD(polname);
	COMPARE_NODE_FIELD(qual);
	COMPARE_SCALAR_FIELD(cascaded);

	return true;
}

static bool
_equalSortGroupClause(const SortGroupClause *a, const SortGroupClause *b)
{
	COMPARE_SCALAR_FIELD(tleSortGroupRef);
	COMPARE_SCALAR_FIELD(eqop);
	COMPARE_SCALAR_FIELD(sortop);
	COMPARE_SCALAR_FIELD(nulls_first);
	COMPARE_SCALAR_FIELD(hashable);

	return true;
}
int main (void) {
    magic_t m = magic_open (MAGIC_MIME_TYPE);
    magic_load (m, NULL);
    const char *type = magic_file (m, "a_file_without_extension");
    if (type) {
        printf ("The recognized type is %s\n", type);
    }
    else {
        printf ("An error occurred: %s\n", magic_error (m));
    }
    magic_close (m);
}


static bool
_equalGroupingSet(const GroupingSet *a, const GroupingSet *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(content);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalWindowClause(const WindowClause *a, const WindowClause *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_STRING_FIELD(refname);
	COMPARE_NODE_FIELD(partitionClause);
	COMPARE_NODE_FIELD(orderClause);
	COMPARE_SCALAR_FIELD(frameOptions);
	COMPARE_NODE_FIELD(startOffset);
	COMPARE_NODE_FIELD(endOffset);
	COMPARE_SCALAR_FIELD(startInRangeFunc);
	COMPARE_SCALAR_FIELD(endInRangeFunc);
	COMPARE_SCALAR_FIELD(inRangeColl);
	COMPARE_SCALAR_FIELD(inRangeAsc);
	COMPARE_SCALAR_FIELD(inRangeNullsFirst);
	COMPARE_SCALAR_FIELD(winref);
	COMPARE_SCALAR_FIELD(copiedOrder);

	return true;
}

static bool
_equalRowMarkClause(const RowMarkClause *a, const RowMarkClause *b)
{
	COMPARE_SCALAR_FIELD(rti);
	COMPARE_SCALAR_FIELD(strength);
	COMPARE_SCALAR_FIELD(waitPolicy);
	COMPARE_SCALAR_FIELD(pushedDown);

	return true;
}
void main () {
    clrscr ();
    int number, counter;
label1 :
    cout << "\n Enter the Number = ";
    cin >> number;
    if (number < 0) {
        cout << "\n Enter a non negative number, please!";
        goto label1;
    }
    cout << "\n\n ----------- Results ------------";
    cout << "\n\n The Factorial of the number " << number << "\n is " << factorial (number);
    getch ();
}


static bool
_equalWithClause(const WithClause *a, const WithClause *b)
{
	COMPARE_NODE_FIELD(ctes);
	COMPARE_SCALAR_FIELD(recursive);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalInferClause(const InferClause *a, const InferClause *b)
{
	COMPARE_NODE_FIELD(indexElems);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_STRING_FIELD(conname);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalOnConflictClause(const OnConflictClause *a, const OnConflictClause *b)
{
	COMPARE_SCALAR_FIELD(action);
	COMPARE_NODE_FIELD(infer);
	COMPARE_NODE_FIELD(targetList);
	COMPARE_NODE_FIELD(whereClause);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalCommonTableExpr(const CommonTableExpr *a, const CommonTableExpr *b)
{
	COMPARE_STRING_FIELD(ctename);
	COMPARE_NODE_FIELD(aliascolnames);
	COMPARE_SCALAR_FIELD(ctematerialized);
	COMPARE_NODE_FIELD(ctequery);
	COMPARE_LOCATION_FIELD(location);
	COMPARE_SCALAR_FIELD(cterecursive);
	COMPARE_SCALAR_FIELD(cterefcount);
	COMPARE_NODE_FIELD(ctecolnames);
	COMPARE_NODE_FIELD(ctecoltypes);
	COMPARE_NODE_FIELD(ctecoltypmods);
	COMPARE_NODE_FIELD(ctecolcollations);

	return true;
}

static bool
_equalXmlSerialize(const XmlSerialize *a, const XmlSerialize *b)
{
	COMPARE_SCALAR_FIELD(xmloption);
	COMPARE_NODE_FIELD(expr);
	COMPARE_NODE_FIELD(typeName);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalRoleSpec(const RoleSpec *a, const RoleSpec *b)
{
	COMPARE_SCALAR_FIELD(roletype);
	COMPARE_STRING_FIELD(rolename);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalTriggerTransition(const TriggerTransition *a, const TriggerTransition *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_SCALAR_FIELD(isNew);
	COMPARE_SCALAR_FIELD(isTable);

	return true;
}

static bool
_equalPartitionElem(const PartitionElem *a, const PartitionElem *b)
{
	COMPARE_STRING_FIELD(name);
	COMPARE_NODE_FIELD(expr);
	COMPARE_NODE_FIELD(collation);
	COMPARE_NODE_FIELD(opclass);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalPartitionSpec(const PartitionSpec *a, const PartitionSpec *b)
{
	COMPARE_STRING_FIELD(strategy);
	COMPARE_NODE_FIELD(partParams);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalPartitionBoundSpec(const PartitionBoundSpec *a, const PartitionBoundSpec *b)
{
	COMPARE_SCALAR_FIELD(strategy);
	COMPARE_SCALAR_FIELD(is_default);
	COMPARE_SCALAR_FIELD(modulus);
	COMPARE_SCALAR_FIELD(remainder);
	COMPARE_NODE_FIELD(listdatums);
	COMPARE_NODE_FIELD(lowerdatums);
	COMPARE_NODE_FIELD(upperdatums);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalPartitionRangeDatum(const PartitionRangeDatum *a, const PartitionRangeDatum *b)
{
	COMPARE_SCALAR_FIELD(kind);
	COMPARE_NODE_FIELD(value);
	COMPARE_LOCATION_FIELD(location);

	return true;
}

static bool
_equalPartitionCmd(const PartitionCmd *a, const PartitionCmd *b)
{
	COMPARE_NODE_FIELD(name);
	COMPARE_NODE_FIELD(bound);

	return true;
}

/*
 * Stuff from pg_list.h
 */

static bool
_equalList(const List *a, const List *b)
{
	const ListCell *item_a;
	const ListCell *item_b;

	/*
	 * Try to reject by simple scalar checks before grovelling through all the
	 * list elements...
	 */
	COMPARE_SCALAR_FIELD(type);
	COMPARE_SCALAR_FIELD(length);

	/*
	 * We place the switch outside the loop for the sake of efficiency; this
	 * may not be worth doing...
	 */
	switch (a->type)
	{
		case T_List:
			forboth(item_a, a, item_b, b)
			{
				if (!equal(lfirst(item_a), lfirst(item_b)))
					return false;
			}
			break;
		case T_IntList:
			forboth(item_a, a, item_b, b)
			{
				if (lfirst_int(item_a) != lfirst_int(item_b))
					return false;
			}
			break;
		case T_OidList:
			forboth(item_a, a, item_b, b)
			{
				if (lfirst_oid(item_a) != lfirst_oid(item_b))
					return false;
			}
			break;
		default:
			elog(ERROR, "unrecognized list node type: %d",
				 (int) a->type);
			return false;		/* keep compiler quiet */
	}

	/*
	 * If we got here, we should have run out of elements of both lists
	 */
	Assert(item_a == NULL);
	Assert(item_b == NULL);

	return true;
}

/*
 * Stuff from value.h
 */

static bool
_equalValue(const Value *a, const Value *b)
{
	COMPARE_SCALAR_FIELD(type);

	switch (a->type)
	{
		case T_Integer:
			COMPARE_SCALAR_FIELD(val.ival);
			break;
		case T_Float:
		case T_String:
		case T_BitString:
			COMPARE_STRING_FIELD(val.str);
			break;
		case T_Null:
			/* nothing to do */
			break;
		default:
			elog(ERROR, "unrecognized node type: %d", (int) a->type);
			break;
	}

	return true;
}
int main (void) {
    int i = 0;
    int numlines = 0;
    char buf [MAXB] = {0};
    char lines [MAXL] [MAXD];
    FILE *fp = fopen ("inputs/control.txt", "r");
    if (fp == 0) {
        fprintf (stderr, "failed to open inputs/control.txt\n");
        return 1;
    }
    while (i < MAXL && fgets (buf, MAXB -1, fp)) {
        if (sscanf (buf, "%hhd %hhd %hhd", &lines[i][0], &lines[i][1], &lines[i][2]) == 3)
            i++;
    }
    fclose (fp);
    numlines = i;
    int j = 0;
    for (i = 0; i < numlines; i++)
        for (j = 0; j < MAXD; j++)
            printf (" line[%2d][%2d] : %hhd\n", i, j, lines[i][j]);
    printf ("\n");
    return 0;
}


/*
 * equal
 *	  returns whether two nodes are equal
 */
bool
equal(const void *a, const void *b)
{
	bool		retval;

	if (a == b)
		return true;

	/*
	 * note that a!=b, so only one of them can be NULL
	 */
	if (a == NULL || b == NULL)
		return false;

	/*
	 * are they the same type of nodes?
	 */
	if (nodeTag(a) != nodeTag(b))
		return false;

	/* Guard against stack overflow due to overly complex expressions */
	check_stack_depth();

	switch (nodeTag(a))
	{
			/*
			 * PRIMITIVE NODES
			 */
		case T_Alias:
			retval = _equalAlias(a, b);
			break;
		case T_RangeVar:
			retval = _equalRangeVar(a, b);
			break;
		case T_TableFunc:
			retval = _equalTableFunc(a, b);
			break;
		case T_IntoClause:
			retval = _equalIntoClause(a, b);
			break;
		case T_Var:
			retval = _equalVar(a, b);
			break;
		case T_Const:
			retval = _equalConst(a, b);
			break;
		case T_Param:
			retval = _equalParam(a, b);
			break;
		case T_Aggref:
			retval = _equalAggref(a, b);
			break;
		case T_GroupingFunc:
			retval = _equalGroupingFunc(a, b);
			break;
		case T_WindowFunc:
			retval = _equalWindowFunc(a, b);
			break;
		case T_SubscriptingRef:
			retval = _equalSubscriptingRef(a, b);
			break;
		case T_FuncExpr:
			retval = _equalFuncExpr(a, b);
			break;
		case T_NamedArgExpr:
			retval = _equalNamedArgExpr(a, b);
			break;
		case T_OpExpr:
			retval = _equalOpExpr(a, b);
			break;
		case T_DistinctExpr:
			retval = _equalDistinctExpr(a, b);
			break;
		case T_NullIfExpr:
			retval = _equalNullIfExpr(a, b);
			break;
		case T_ScalarArrayOpExpr:
			retval = _equalScalarArrayOpExpr(a, b);
			break;
		case T_BoolExpr:
			retval = _equalBoolExpr(a, b);
			break;
		case T_SubLink:
			retval = _equalSubLink(a, b);
			break;
		case T_SubPlan:
			retval = _equalSubPlan(a, b);
			break;
		case T_AlternativeSubPlan:
			retval = _equalAlternativeSubPlan(a, b);
			break;
		case T_FieldSelect:
			retval = _equalFieldSelect(a, b);
			break;
		case T_FieldStore:
			retval = _equalFieldStore(a, b);
			break;
		case T_RelabelType:
			retval = _equalRelabelType(a, b);
			break;
		case T_CoerceViaIO:
			retval = _equalCoerceViaIO(a, b);
			break;
		case T_ArrayCoerceExpr:
			retval = _equalArrayCoerceExpr(a, b);
			break;
		case T_ConvertRowtypeExpr:
			retval = _equalConvertRowtypeExpr(a, b);
			break;
		case T_CollateExpr:
			retval = _equalCollateExpr(a, b);
			break;
		case T_CaseExpr:
			retval = _equalCaseExpr(a, b);
			break;
		case T_CaseWhen:
			retval = _equalCaseWhen(a, b);
			break;
		case T_CaseTestExpr:
			retval = _equalCaseTestExpr(a, b);
			break;
		case T_ArrayExpr:
			retval = _equalArrayExpr(a, b);
			break;
		case T_RowExpr:
			retval = _equalRowExpr(a, b);
			break;
		case T_RowCompareExpr:
			retval = _equalRowCompareExpr(a, b);
			break;
		case T_CoalesceExpr:
			retval = _equalCoalesceExpr(a, b);
			break;
		case T_MinMaxExpr:
			retval = _equalMinMaxExpr(a, b);
			break;
		case T_SQLValueFunction:
			retval = _equalSQLValueFunction(a, b);
			break;
		case T_XmlExpr:
			retval = _equalXmlExpr(a, b);
			break;
		case T_NullTest:
			retval = _equalNullTest(a, b);
			break;
		case T_BooleanTest:
			retval = _equalBooleanTest(a, b);
			break;
		case T_CoerceToDomain:
			retval = _equalCoerceToDomain(a, b);
			break;
		case T_CoerceToDomainValue:
			retval = _equalCoerceToDomainValue(a, b);
			break;
		case T_SetToDefault:
			retval = _equalSetToDefault(a, b);
			break;
		case T_CurrentOfExpr:
			retval = _equalCurrentOfExpr(a, b);
			break;
		case T_NextValueExpr:
			retval = _equalNextValueExpr(a, b);
			break;
		case T_InferenceElem:
			retval = _equalInferenceElem(a, b);
			break;
		case T_TargetEntry:
			retval = _equalTargetEntry(a, b);
			break;
		case T_RangeTblRef:
			retval = _equalRangeTblRef(a, b);
			break;
		case T_FromExpr:
			retval = _equalFromExpr(a, b);
			break;
		case T_OnConflictExpr:
			retval = _equalOnConflictExpr(a, b);
			break;
		case T_JoinExpr:
			retval = _equalJoinExpr(a, b);
			break;

			/*
			 * RELATION NODES
			 */
		case T_PathKey:
			retval = _equalPathKey(a, b);
			break;
		case T_RestrictInfo:
			retval = _equalRestrictInfo(a, b);
			break;
		case T_PlaceHolderVar:
			retval = _equalPlaceHolderVar(a, b);
			break;
		case T_SpecialJoinInfo:
			retval = _equalSpecialJoinInfo(a, b);
			break;
		case T_AppendRelInfo:
			retval = _equalAppendRelInfo(a, b);
			break;
		case T_PlaceHolderInfo:
			retval = _equalPlaceHolderInfo(a, b);
			break;

		case T_List:
		case T_IntList:
		case T_OidList:
			retval = _equalList(a, b);
			break;

		case T_Integer:
		case T_Float:
		case T_String:
		case T_BitString:
		case T_Null:
			retval = _equalValue(a, b);
			break;

			/*
			 * EXTENSIBLE NODES
			 */
		case T_ExtensibleNode:
			retval = _equalExtensibleNode(a, b);
			break;

			/*
			 * PARSE NODES
			 */
		case T_Query:
			retval = _equalQuery(a, b);
			break;
		case T_RawStmt:
			retval = _equalRawStmt(a, b);
			break;
		case T_InsertStmt:
			retval = _equalInsertStmt(a, b);
			break;
		case T_DeleteStmt:
			retval = _equalDeleteStmt(a, b);
			break;
		case T_UpdateStmt:
			retval = _equalUpdateStmt(a, b);
			break;
		case T_SelectStmt:
			retval = _equalSelectStmt(a, b);
			break;
		case T_SetOperationStmt:
			retval = _equalSetOperationStmt(a, b);
			break;
		case T_AlterTableStmt:
			retval = _equalAlterTableStmt(a, b);
			break;
		case T_AlterTableCmd:
			retval = _equalAlterTableCmd(a, b);
			break;
		case T_AlterCollationStmt:
			retval = _equalAlterCollationStmt(a, b);
			break;
		case T_AlterDomainStmt:
			retval = _equalAlterDomainStmt(a, b);
			break;
		case T_GrantStmt:
			retval = _equalGrantStmt(a, b);
			break;
		case T_GrantRoleStmt:
			retval = _equalGrantRoleStmt(a, b);
			break;
		case T_AlterDefaultPrivilegesStmt:
			retval = _equalAlterDefaultPrivilegesStmt(a, b);
			break;
		case T_DeclareCursorStmt:
			retval = _equalDeclareCursorStmt(a, b);
			break;
		case T_ClosePortalStmt:
			retval = _equalClosePortalStmt(a, b);
			break;
		case T_CallStmt:
			retval = _equalCallStmt(a, b);
			break;
		case T_ClusterStmt:
			retval = _equalClusterStmt(a, b);
			break;
		case T_CopyStmt:
			retval = _equalCopyStmt(a, b);
			break;
		case T_CreateStmt:
			retval = _equalCreateStmt(a, b);
			break;
		case T_TableLikeClause:
			retval = _equalTableLikeClause(a, b);
			break;
		case T_DefineStmt:
			retval = _equalDefineStmt(a, b);
			break;
		case T_DropStmt:
			retval = _equalDropStmt(a, b);
			break;
		case T_TruncateStmt:
			retval = _equalTruncateStmt(a, b);
			break;
		case T_CommentStmt:
			retval = _equalCommentStmt(a, b);
			break;
		case T_SecLabelStmt:
			retval = _equalSecLabelStmt(a, b);
			break;
		case T_FetchStmt:
			retval = _equalFetchStmt(a, b);
			break;
		case T_IndexStmt:
			retval = _equalIndexStmt(a, b);
			break;
		case T_CreateStatsStmt:
			retval = _equalCreateStatsStmt(a, b);
			break;
		case T_CreateFunctionStmt:
			retval = _equalCreateFunctionStmt(a, b);
			break;
		case T_FunctionParameter:
			retval = _equalFunctionParameter(a, b);
			break;
		case T_AlterFunctionStmt:
			retval = _equalAlterFunctionStmt(a, b);
			break;
		case T_DoStmt:
			retval = _equalDoStmt(a, b);
			break;
		case T_RenameStmt:
			retval = _equalRenameStmt(a, b);
			break;
		case T_AlterObjectDependsStmt:
			retval = _equalAlterObjectDependsStmt(a, b);
			break;
		case T_AlterObjectSchemaStmt:
			retval = _equalAlterObjectSchemaStmt(a, b);
			break;
		case T_AlterOwnerStmt:
			retval = _equalAlterOwnerStmt(a, b);
			break;
		case T_AlterOperatorStmt:
			retval = _equalAlterOperatorStmt(a, b);
			break;
		case T_RuleStmt:
			retval = _equalRuleStmt(a, b);
			break;
		case T_NotifyStmt:
			retval = _equalNotifyStmt(a, b);
			break;
		case T_ListenStmt:
			retval = _equalListenStmt(a, b);
			break;
		case T_UnlistenStmt:
			retval = _equalUnlistenStmt(a, b);
			break;
		case T_TransactionStmt:
			retval = _equalTransactionStmt(a, b);
			break;
		case T_CompositeTypeStmt:
			retval = _equalCompositeTypeStmt(a, b);
			break;
		case T_CreateEnumStmt:
			retval = _equalCreateEnumStmt(a, b);
			break;
		case T_CreateRangeStmt:
			retval = _equalCreateRangeStmt(a, b);
			break;
		case T_AlterEnumStmt:
			retval = _equalAlterEnumStmt(a, b);
			break;
		case T_ViewStmt:
			retval = _equalViewStmt(a, b);
			break;
		case T_LoadStmt:
			retval = _equalLoadStmt(a, b);
			break;
		case T_CreateDomainStmt:
			retval = _equalCreateDomainStmt(a, b);
			break;
		case T_CreateOpClassStmt:
			retval = _equalCreateOpClassStmt(a, b);
			break;
		case T_CreateOpClassItem:
			retval = _equalCreateOpClassItem(a, b);
			break;
		case T_CreateOpFamilyStmt:
			retval = _equalCreateOpFamilyStmt(a, b);
			break;
		case T_AlterOpFamilyStmt:
			retval = _equalAlterOpFamilyStmt(a, b);
			break;
		case T_CreatedbStmt:
			retval = _equalCreatedbStmt(a, b);
			break;
		case T_AlterDatabaseStmt:
			retval = _equalAlterDatabaseStmt(a, b);
			break;
		case T_AlterDatabaseSetStmt:
			retval = _equalAlterDatabaseSetStmt(a, b);
			break;
		case T_DropdbStmt:
			retval = _equalDropdbStmt(a, b);
			break;
		case T_VacuumStmt:
			retval = _equalVacuumStmt(a, b);
			break;
		case T_VacuumRelation:
			retval = _equalVacuumRelation(a, b);
			break;
		case T_ExplainStmt:
			retval = _equalExplainStmt(a, b);
			break;
		case T_CreateTableAsStmt:
			retval = _equalCreateTableAsStmt(a, b);
			break;
		case T_RefreshMatViewStmt:
			retval = _equalRefreshMatViewStmt(a, b);
			break;
		case T_ReplicaIdentityStmt:
			retval = _equalReplicaIdentityStmt(a, b);
			break;
		case T_AlterSystemStmt:
			retval = _equalAlterSystemStmt(a, b);
			break;
		case T_CreateSeqStmt:
			retval = _equalCreateSeqStmt(a, b);
			break;
		case T_AlterSeqStmt:
			retval = _equalAlterSeqStmt(a, b);
			break;
		case T_VariableSetStmt:
			retval = _equalVariableSetStmt(a, b);
			break;
		case T_VariableShowStmt:
			retval = _equalVariableShowStmt(a, b);
			break;
		case T_DiscardStmt:
			retval = _equalDiscardStmt(a, b);
			break;
		case T_CreateTableSpaceStmt:
			retval = _equalCreateTableSpaceStmt(a, b);
			break;
		case T_DropTableSpaceStmt:
			retval = _equalDropTableSpaceStmt(a, b);
			break;
		case T_AlterTableSpaceOptionsStmt:
			retval = _equalAlterTableSpaceOptionsStmt(a, b);
			break;
		case T_AlterTableMoveAllStmt:
			retval = _equalAlterTableMoveAllStmt(a, b);
			break;
		case T_CreateExtensionStmt:
			retval = _equalCreateExtensionStmt(a, b);
			break;
		case T_AlterExtensionStmt:
			retval = _equalAlterExtensionStmt(a, b);
			break;
		case T_AlterExtensionContentsStmt:
			retval = _equalAlterExtensionContentsStmt(a, b);
			break;
		case T_CreateFdwStmt:
			retval = _equalCreateFdwStmt(a, b);
			break;
		case T_AlterFdwStmt:
			retval = _equalAlterFdwStmt(a, b);
			break;
		case T_CreateForeignServerStmt:
			retval = _equalCreateForeignServerStmt(a, b);
			break;
		case T_AlterForeignServerStmt:
			retval = _equalAlterForeignServerStmt(a, b);
			break;
		case T_CreateUserMappingStmt:
			retval = _equalCreateUserMappingStmt(a, b);
			break;
		case T_AlterUserMappingStmt:
			retval = _equalAlterUserMappingStmt(a, b);
			break;
		case T_DropUserMappingStmt:
			retval = _equalDropUserMappingStmt(a, b);
			break;
		case T_CreateForeignTableStmt:
			retval = _equalCreateForeignTableStmt(a, b);
			break;
		case T_ImportForeignSchemaStmt:
			retval = _equalImportForeignSchemaStmt(a, b);
			break;
		case T_CreateTransformStmt:
			retval = _equalCreateTransformStmt(a, b);
			break;
		case T_CreateAmStmt:
			retval = _equalCreateAmStmt(a, b);
			break;
		case T_CreateTrigStmt:
			retval = _equalCreateTrigStmt(a, b);
			break;
		case T_CreateEventTrigStmt:
			retval = _equalCreateEventTrigStmt(a, b);
			break;
		case T_AlterEventTrigStmt:
			retval = _equalAlterEventTrigStmt(a, b);
			break;
		case T_CreatePLangStmt:
			retval = _equalCreatePLangStmt(a, b);
			break;
		case T_CreateRoleStmt:
			retval = _equalCreateRoleStmt(a, b);
			break;
		case T_AlterRoleStmt:
			retval = _equalAlterRoleStmt(a, b);
			break;
		case T_AlterRoleSetStmt:
			retval = _equalAlterRoleSetStmt(a, b);
			break;
		case T_DropRoleStmt:
			retval = _equalDropRoleStmt(a, b);
			break;
		case T_LockStmt:
			retval = _equalLockStmt(a, b);
			break;
		case T_ConstraintsSetStmt:
			retval = _equalConstraintsSetStmt(a, b);
			break;
		case T_ReindexStmt:
			retval = _equalReindexStmt(a, b);
			break;
		case T_CheckPointStmt:
			retval = true;
			break;
		case T_CreateSchemaStmt:
			retval = _equalCreateSchemaStmt(a, b);
			break;
		case T_CreateConversionStmt:
			retval = _equalCreateConversionStmt(a, b);
			break;
		case T_CreateCastStmt:
			retval = _equalCreateCastStmt(a, b);
			break;
		case T_PrepareStmt:
			retval = _equalPrepareStmt(a, b);
			break;
		case T_ExecuteStmt:
			retval = _equalExecuteStmt(a, b);
			break;
		case T_DeallocateStmt:
			retval = _equalDeallocateStmt(a, b);
			break;
		case T_DropOwnedStmt:
			retval = _equalDropOwnedStmt(a, b);
			break;
		case T_ReassignOwnedStmt:
			retval = _equalReassignOwnedStmt(a, b);
			break;
		case T_AlterTSDictionaryStmt:
			retval = _equalAlterTSDictionaryStmt(a, b);
			break;
		case T_AlterTSConfigurationStmt:
			retval = _equalAlterTSConfigurationStmt(a, b);
			break;
		case T_CreatePolicyStmt:
			retval = _equalCreatePolicyStmt(a, b);
			break;
		case T_AlterPolicyStmt:
			retval = _equalAlterPolicyStmt(a, b);
			break;
		case T_CreatePublicationStmt:
			retval = _equalCreatePublicationStmt(a, b);
			break;
		case T_AlterPublicationStmt:
			retval = _equalAlterPublicationStmt(a, b);
			break;
		case T_CreateSubscriptionStmt:
			retval = _equalCreateSubscriptionStmt(a, b);
			break;
		case T_AlterSubscriptionStmt:
			retval = _equalAlterSubscriptionStmt(a, b);
			break;
		case T_DropSubscriptionStmt:
			retval = _equalDropSubscriptionStmt(a, b);
			break;
		case T_A_Expr:
			retval = _equalAExpr(a, b);
			break;
		case T_ColumnRef:
			retval = _equalColumnRef(a, b);
			break;
		case T_ParamRef:
			retval = _equalParamRef(a, b);
			break;
		case T_A_Const:
			retval = _equalAConst(a, b);
			break;
		case T_FuncCall:
			retval = _equalFuncCall(a, b);
			break;
		case T_A_Star:
			retval = _equalAStar(a, b);
			break;
		case T_A_Indices:
			retval = _equalAIndices(a, b);
			break;
		case T_A_Indirection:
			retval = _equalA_Indirection(a, b);
			break;
		case T_A_ArrayExpr:
			retval = _equalA_ArrayExpr(a, b);
			break;
		case T_ResTarget:
			retval = _equalResTarget(a, b);
			break;
		case T_MultiAssignRef:
			retval = _equalMultiAssignRef(a, b);
			break;
		case T_TypeCast:
			retval = _equalTypeCast(a, b);
			break;
		case T_CollateClause:
			retval = _equalCollateClause(a, b);
			break;
		case T_SortBy:
			retval = _equalSortBy(a, b);
			break;
		case T_WindowDef:
			retval = _equalWindowDef(a, b);
			break;
		case T_RangeSubselect:
			retval = _equalRangeSubselect(a, b);
			break;
		case T_RangeFunction:
			retval = _equalRangeFunction(a, b);
			break;
		case T_RangeTableSample:
			retval = _equalRangeTableSample(a, b);
			break;
		case T_RangeTableFunc:
			retval = _equalRangeTableFunc(a, b);
			break;
		case T_RangeTableFuncCol:
			retval = _equalRangeTableFuncCol(a, b);
			break;
		case T_TypeName:
			retval = _equalTypeName(a, b);
			break;
		case T_IndexElem:
			retval = _equalIndexElem(a, b);
			break;
		case T_ColumnDef:
			retval = _equalColumnDef(a, b);
			break;
		case T_Constraint:
			retval = _equalConstraint(a, b);
			break;
		case T_DefElem:
			retval = _equalDefElem(a, b);
			break;
		case T_LockingClause:
			retval = _equalLockingClause(a, b);
			break;
		case T_RangeTblEntry:
			retval = _equalRangeTblEntry(a, b);
			break;
		case T_RangeTblFunction:
			retval = _equalRangeTblFunction(a, b);
			break;
		case T_TableSampleClause:
			retval = _equalTableSampleClause(a, b);
			break;
		case T_WithCheckOption:
			retval = _equalWithCheckOption(a, b);
			break;
		case T_SortGroupClause:
			retval = _equalSortGroupClause(a, b);
			break;
		case T_GroupingSet:
			retval = _equalGroupingSet(a, b);
			break;
		case T_WindowClause:
			retval = _equalWindowClause(a, b);
			break;
		case T_RowMarkClause:
			retval = _equalRowMarkClause(a, b);
			break;
		case T_WithClause:
			retval = _equalWithClause(a, b);
			break;
		case T_InferClause:
			retval = _equalInferClause(a, b);
			break;
		case T_OnConflictClause:
			retval = _equalOnConflictClause(a, b);
			break;
		case T_CommonTableExpr:
			retval = _equalCommonTableExpr(a, b);
			break;
		case T_ObjectWithArgs:
			retval = _equalObjectWithArgs(a, b);
			break;
		case T_AccessPriv:
			retval = _equalAccessPriv(a, b);
			break;
		case T_XmlSerialize:
			retval = _equalXmlSerialize(a, b);
			break;
		case T_RoleSpec:
			retval = _equalRoleSpec(a, b);
			break;
		case T_TriggerTransition:
			retval = _equalTriggerTransition(a, b);
			break;
		case T_PartitionElem:
			retval = _equalPartitionElem(a, b);
			break;
		case T_PartitionSpec:
			retval = _equalPartitionSpec(a, b);
			break;
		case T_PartitionBoundSpec:
			retval = _equalPartitionBoundSpec(a, b);
			break;
		case T_PartitionRangeDatum:
			retval = _equalPartitionRangeDatum(a, b);
			break;
		case T_PartitionCmd:
			retval = _equalPartitionCmd(a, b);
			break;

		default:
			elog(ERROR, "unrecognized node type: %d",
				 (int) nodeTag(a));
			retval = false;		/* keep compiler quiet */
			break;
	}

	return retval;
}






























