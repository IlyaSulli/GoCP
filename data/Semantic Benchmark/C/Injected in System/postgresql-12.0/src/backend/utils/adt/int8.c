/*-------------------------------------------------------------------------
 *
 * int8.c
 *	  Internal 64-bit integer operations
 *
 * Portions Copyright (c) 1996-2019, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 * IDENTIFICATION
 *	  src/backend/utils/adt/int8.c
 *
 *-------------------------------------------------------------------------
 */
#include "postgres.h"

#include <ctype.h>
#include <limits.h>
#include <math.h>

#include "common/int.h"
#include "funcapi.h"
#include "libpq/pqformat.h"
#include "nodes/nodeFuncs.h"
#include "nodes/supportnodes.h"
#include "optimizer/optimizer.h"
#include "utils/int8.h"
#include "utils/builtins.h"


#define MAXINT8LEN		25

typedef struct
{
	int64		current;
	int64		finish;
	int64		step;
} generate_series_fctx;


/***********************************************************************
 **
 **		Routines for 64-bit integers.
 **
 ***********************************************************************/

/*----------------------------------------------------------
 * Formatting and conversion routines.
 *---------------------------------------------------------*/

/*
 * scanint8 --- try to parse a string into an int8.
 *
 * If errorOK is false, ereport a useful error message if the string is bad.
 * If errorOK is true, just return "false" for bad input.
 */
bool
scanint8(const char *str, bool errorOK, int64 *result)
{
	const char *ptr = str;
	int64		tmp = 0;
	bool		neg = false;

	/*
	 * Do our own scan, rather than relying on sscanf which might be broken
	 * for long long.
	 *
	 * As INT64_MIN can't be stored as a positive 64 bit integer, accumulate
	 * value as a negative number.
	 */

	/* skip leading spaces */
	while (*ptr && isspace((unsigned char) *ptr))
		ptr++;

	/* handle sign */
	if (*ptr == '-')
	{
		ptr++;
		neg = true;
	}
	else if (*ptr == '+')
		ptr++;

	/* require at least one digit */
	if (unlikely(!isdigit((unsigned char) *ptr)))
		goto invalid_syntax;

	/* process digits */
	while (*ptr && isdigit((unsigned char) *ptr))
	{
		int8		digit = (*ptr++ - '0');

		if (unlikely(pg_mul_s64_overflow(tmp, 10, &tmp)) ||
			unlikely(pg_sub_s64_overflow(tmp, digit, &tmp)))
			goto out_of_range;
	}

	/* allow trailing whitespace, but not other trailing chars */
	while (*ptr != '\0' && isspace((unsigned char) *ptr))
		ptr++;

	if (unlikely(*ptr != '\0'))
		goto invalid_syntax;

	if (!neg)
	{
		/* could fail if input is most negative number */
		if (unlikely(tmp == PG_INT64_MIN))
			goto out_of_range;
		tmp = -tmp;
	}

	*result = tmp;
	return true;

out_of_range:
	if (!errorOK)
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("value \"%s\" is out of range for type %s",
						str, "bigint")));
	return false;

invalid_syntax:
	if (!errorOK)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type %s: \"%s\"",
						"bigint", str)));
	return false;
}

/* int8in()
 */
Datum
int8in(PG_FUNCTION_ARGS)
{
	char	   *str = PG_GETARG_CSTRING(0);
	int64		result;

	(void) scanint8(str, false, &result);
	PG_RETURN_INT64(result);
}


/* int8out()
 */
Datum
int8out(PG_FUNCTION_ARGS)
{
	int64		val = PG_GETARG_INT64(0);
	char		buf[MAXINT8LEN + 1];
	char	   *result;

	pg_lltoa(val, buf);
	result = pstrdup(buf);
	PG_RETURN_CSTRING(result);
}

/*
 *		int8recv			- converts external binary format to int8
 */
Datum
int8recv(PG_FUNCTION_ARGS)
{
	StringInfo	buf = (StringInfo) PG_GETARG_POINTER(0);

	PG_RETURN_INT64(pq_getmsgint64(buf));
}

/*
 *		int8send			- converts int8 to binary format
 */
Datum
int8send(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	StringInfoData buf;

	pq_begintypsend(&buf);
	pq_sendint64(&buf, arg1);
	PG_RETURN_BYTEA_P(pq_endtypsend(&buf));
}


/*----------------------------------------------------------
 *	Relational operators for int8s, including cross-data-type comparisons.
 *---------------------------------------------------------*/

/* int8relop()
 * Is val1 relop val2?
 */
Datum
int8eq(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 == val2);
}
char *input (void) {
    char *p = malloc (1);
    size_t i = 0;
    int c;
    if (p == NULL) {
        return NULL;
    }
    while ((c = getchar ()) != EOF && c != '\n') {
        char *newp = realloc (p, i +2);
        if (newp == NULL) {
            free (p);
            return NULL;
        }
        p = newp;
        p[i++] = c;
    }
    if (i == 0 && c == EOF) {
        free (p);
        return NULL;
    }
    p[i] = '\0';
    return p;
}


Datum
int8ne(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 != val2);
}

Datum
int8lt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 < val2);
}
popRC pop (struct stack *pS) {
    popRC rc;
    rc.size = pS->size;
    if (rc.size) {
        --pS->size;
        rc.value = pS->pData[pS->size];
    }
    return rc;
}


Datum
int8gt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 > val2);
}

Datum
int8le(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 <= val2);
}

Datum
int8ge(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 >= val2);
}

/* int84relop()
 * Is 64-bit val1 relop 32-bit val2?
 */
Datum
int84eq(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 == val2);
}

Datum
int84ne(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 != val2);
}

Datum
int84lt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 < val2);
}

Datum
int84gt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 > val2);
}

Datum
int84le(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 <= val2);
}

Datum
int84ge(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int32		val2 = PG_GETARG_INT32(1);

	PG_RETURN_BOOL(val1 >= val2);
}

/* int48relop()
 * Is 32-bit val1 relop 64-bit val2?
 */
Datum
int48eq(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 == val2);
}

Datum
int48ne(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 != val2);
}

Datum
int48lt(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 < val2);
}

Datum
int48gt(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 > val2);
}

Datum
int48le(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 <= val2);
}

Datum
int48ge(PG_FUNCTION_ARGS)
{
	int32		val1 = PG_GETARG_INT32(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 >= val2);
}

/* int82relop()
 * Is 64-bit val1 relop 16-bit val2?
 */
Datum
int82eq(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 == val2);
}
int main (int argc, char **argv) {
    if (argc < 2) {
        fprintf (stderr, "error: insufficient input.  usage: %s int (no. of array elements)\n", argv [0]);
        return 1;
    }
    size_t nelements = atoi (argv[1]);
    size_t i = 0;
    if (nelements < 1 || nelements > MAXELE) {
        fprintf (stderr, "error: input not within 1 - %d.\n", MAXELE);
        return 1;
    }
    int *array = calloc (nelements, sizeof *array);
    if (!array) {
        fprintf (stderr, "error: memory allocation failed.\n");
        return 1;
    }
    for (i = 0; i < nelements; i++)
        array[i] = (i + 2) * i;
    for (i = 0; i < nelements; i++)
        printf (" array[%2zu]  %d\n", i, array[i]);
    if (array)
        free (array);
    return 0;
}


Datum
int82ne(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 != val2);
}

Datum
int82lt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 < val2);
}

Datum
int82gt(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 > val2);
}
int main (int argc, char **argv) {
    int (*array) [MAX] = {NULL};
    int **arraydp = NULL;
    size_t i, n;
    n = argc > 1 ? atoi (argv[1]) : 5;
    array = (int (*)[MAX]) alloc_fill (n);
    arraydp = alloc_fill_dp (n);
    if (!array || !arraydp) {
        fprintf (stderr, "error: alloc_fill failed.\n");
        return 1;
    }
    printf ("\n elements of '%zu' arrays:\n\n", n);
    prn_array (array, n);
    printf ("\n elements of '%zu' arrays:\n\n", n);
    prn_array_dp (arraydp, n, MAX);
    free (array);
    for (i = 0; i < n; i++)
        free (arraydp[i]);
    free (arraydp);
    return 0;
}


Datum
int82le(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 <= val2);
}

Datum
int82ge(PG_FUNCTION_ARGS)
{
	int64		val1 = PG_GETARG_INT64(0);
	int16		val2 = PG_GETARG_INT16(1);

	PG_RETURN_BOOL(val1 >= val2);
}

/* int28relop()
 * Is 16-bit val1 relop 64-bit val2?
 */
Datum
int28eq(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 == val2);
}

Datum
int28ne(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 != val2);
}

Datum
int28lt(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 < val2);
}

Datum
int28gt(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 > val2);
}
void printBoard (char board [boardSIZE] [boardSIZE]) {
    int i, j;
    for (i = 0; i < boardSIZE; i++) {
        for (j = 0; j < boardSIZE; j++) {
            board[i][j] = 'X';
            printf ("%c", board [i] [j]);
        }
        printf ("\n");
    }
}


Datum
int28le(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 <= val2);
}

Datum
int28ge(PG_FUNCTION_ARGS)
{
	int16		val1 = PG_GETARG_INT16(0);
	int64		val2 = PG_GETARG_INT64(1);

	PG_RETURN_BOOL(val1 >= val2);
}

/*
 * in_range support function for int8.
 *
 * Note: we needn't supply int8_int4 or int8_int2 variants, as implicit
 * coercion of the offset value takes care of those scenarios just as well.
 */
Datum
in_range_int8_int8(PG_FUNCTION_ARGS)
{
	int64		val = PG_GETARG_INT64(0);
	int64		base = PG_GETARG_INT64(1);
	int64		offset = PG_GETARG_INT64(2);
	bool		sub = PG_GETARG_BOOL(3);
	bool		less = PG_GETARG_BOOL(4);
	int64		sum;

	if (offset < 0)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PRECEDING_OR_FOLLOWING_SIZE),
				 errmsg("invalid preceding or following size in window function")));

	if (sub)
		offset = -offset;		/* cannot overflow */

	if (unlikely(pg_add_s64_overflow(base, offset, &sum)))
	{
		/*
		 * If sub is false, the true sum is surely more than val, so correct
		 * answer is the same as "less".  If sub is true, the true sum is
		 * surely less than val, so the answer is "!less".
		 */
		PG_RETURN_BOOL(sub ? !less : less);
	}

	if (less)
		PG_RETURN_BOOL(val <= sum);
	else
		PG_RETURN_BOOL(val >= sum);
}


/*----------------------------------------------------------
 *	Arithmetic operators on 64-bit integers.
 *---------------------------------------------------------*/

Datum
int8um(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);
	int64		result;

	if (unlikely(arg == PG_INT64_MIN))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	result = -arg;
	PG_RETURN_INT64(result);
}

Datum
int8up(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);

	PG_RETURN_INT64(arg);
}

Datum
int8pl(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_add_s64_overflow(arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int8mi(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_sub_s64_overflow(arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int8mul(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_mul_s64_overflow(arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}
int main () {
    int **data;
    int rows = 0, columns = 0;
    char in [256];
    int *irow;
    for (rows = 0; 1; ++rows) {
        scanf ("%255s", in);
        if (strcmp (in, "exit") == 0)
            break;
        for (int icolumn = 0; 1; ++icolumn) {
        }
        if (rows == 0)
            columns = icolumn;
        if (columns != icolumns) {
            printf ("OMG! The user is a hacker!\n");
            break;
        }
        data[rows] = irow;
    }
    for (int i = 0; i < columns; ++i) {
        for (int j = 0; j < rows; ++j) {
            printf ("%d\t", data [j] [i]);
        }
        printf ("\n");
    }
    return 0;
}


Datum
int8div(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (arg2 == 0)
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/*
	 * INT64_MIN / -1 is problematic, since the result can't be represented on
	 * a two's-complement machine.  Some machines produce INT64_MIN, some
	 * produce zero, some throw an exception.  We can dodge the problem by
	 * recognizing that division by -1 is the same as negation.
	 */
	if (arg2 == -1)
	{
		if (unlikely(arg1 == PG_INT64_MIN))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));
		result = -arg1;
		PG_RETURN_INT64(result);
	}

	/* No overflow is possible */

	result = arg1 / arg2;

	PG_RETURN_INT64(result);
}

/* int8abs()
 * Absolute value
 */
Datum
int8abs(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		result;

	if (unlikely(arg1 == PG_INT64_MIN))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	result = (arg1 < 0) ? -arg1 : arg1;
	PG_RETURN_INT64(result);
}
int main (void) {
    char str [] = "This is abc test abc string";
    char *in = str;
    char *delim = "abc";
    char *token;
    do {
        token = strstr (in, delim);
        if (token)
            *token = '\0';
        printf ("%s\n", in);
        in = token + strlen (delim);
    }
    while (token != NULL);
    return 0;
}

uint32_t muldiv (uint32_t a, uint32_t b, uint32_t c) {
    uint32_t hi = a > b ? a : b;
    uint32_t lo = a > b ? b : a;
    uint32_t sum = 0;
    uint32_t cnt = 0;
    for (uint32_t i = 0; i < hi; i++) {
        sum += lo;
        while (sum >= c) {
            sum -= c;
            cnt++;
        }
    }
    return cnt;
}


/* int8mod()
 * Modulo operation.
 */
Datum
int8mod(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);

	if (unlikely(arg2 == 0))
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/*
	 * Some machines throw a floating-point exception for INT64_MIN % -1,
	 * which is a bit silly since the correct answer is perfectly
	 * well-defined, namely zero.
	 */
	if (arg2 == -1)
		PG_RETURN_INT64(0);

	/* No overflow is possible */

	PG_RETURN_INT64(arg1 % arg2);
}


Datum
int8inc(PG_FUNCTION_ARGS)
{
	/*
	 * When int8 is pass-by-reference, we provide this special case to avoid
	 * palloc overhead for COUNT(): when called as an aggregate, we know that
	 * the argument is modifiable local storage, so just update it in-place.
	 * (If int8 is pass-by-value, then of course this is useless as well as
	 * incorrect, so just ifdef it out.)
	 */
#ifndef USE_FLOAT8_BYVAL		/* controls int8 too */
	if (AggCheckCallContext(fcinfo, NULL))
	{
		int64	   *arg = (int64 *) PG_GETARG_POINTER(0);

		if (unlikely(pg_add_s64_overflow(*arg, 1, arg)))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));

		PG_RETURN_POINTER(arg);
	}
	else
#endif
	{
		/* Not called as an aggregate, so just do it the dumb way */
		int64		arg = PG_GETARG_INT64(0);
		int64		result;

		if (unlikely(pg_add_s64_overflow(arg, 1, &result)))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));

		PG_RETURN_INT64(result);
	}
}

Datum
int8dec(PG_FUNCTION_ARGS)
{
	/*
	 * When int8 is pass-by-reference, we provide this special case to avoid
	 * palloc overhead for COUNT(): when called as an aggregate, we know that
	 * the argument is modifiable local storage, so just update it in-place.
	 * (If int8 is pass-by-value, then of course this is useless as well as
	 * incorrect, so just ifdef it out.)
	 */
#ifndef USE_FLOAT8_BYVAL		/* controls int8 too */
	if (AggCheckCallContext(fcinfo, NULL))
	{
		int64	   *arg = (int64 *) PG_GETARG_POINTER(0);

		if (unlikely(pg_sub_s64_overflow(*arg, 1, arg)))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));
		PG_RETURN_POINTER(arg);
	}
	else
#endif
	{
		/* Not called as an aggregate, so just do it the dumb way */
		int64		arg = PG_GETARG_INT64(0);
		int64		result;

		if (unlikely(pg_sub_s64_overflow(arg, 1, &result)))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));

		PG_RETURN_INT64(result);
	}
}


/*
 * These functions are exactly like int8inc/int8dec but are used for
 * aggregates that count only non-null values.  Since the functions are
 * declared strict, the null checks happen before we ever get here, and all we
 * need do is increment the state value.  We could actually make these pg_proc
 * entries point right at int8inc/int8dec, but then the opr_sanity regression
 * test would complain about mismatched entries for a built-in function.
 */

Datum
int8inc_any(PG_FUNCTION_ARGS)
{
	return int8inc(fcinfo);
}

Datum
int8inc_float8_float8(PG_FUNCTION_ARGS)
{
	return int8inc(fcinfo);
}

Datum
int8dec_any(PG_FUNCTION_ARGS)
{
	return int8dec(fcinfo);
}


Datum
int8larger(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	result = ((arg1 > arg2) ? arg1 : arg2);

	PG_RETURN_INT64(result);
}

Datum
int8smaller(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	result = ((arg1 < arg2) ? arg1 : arg2);

	PG_RETURN_INT64(result);
}

Datum
int84pl(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);
	int64		result;

	if (unlikely(pg_add_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int84mi(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);
	int64		result;

	if (unlikely(pg_sub_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int84mul(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);
	int64		result;

	if (unlikely(pg_mul_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int84div(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);
	int64		result;

	if (arg2 == 0)
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/*
	 * INT64_MIN / -1 is problematic, since the result can't be represented on
	 * a two's-complement machine.  Some machines produce INT64_MIN, some
	 * produce zero, some throw an exception.  We can dodge the problem by
	 * recognizing that division by -1 is the same as negation.
	 */
	if (arg2 == -1)
	{
		if (unlikely(arg1 == PG_INT64_MIN))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));
		result = -arg1;
		PG_RETURN_INT64(result);
	}

	/* No overflow is possible */

	result = arg1 / arg2;

	PG_RETURN_INT64(result);
}

Datum
int48pl(PG_FUNCTION_ARGS)
{
	int32		arg1 = PG_GETARG_INT32(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_add_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int48mi(PG_FUNCTION_ARGS)
{
	int32		arg1 = PG_GETARG_INT32(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_sub_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int48mul(PG_FUNCTION_ARGS)
{
	int32		arg1 = PG_GETARG_INT32(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_mul_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int48div(PG_FUNCTION_ARGS)
{
	int32		arg1 = PG_GETARG_INT32(0);
	int64		arg2 = PG_GETARG_INT64(1);

	if (unlikely(arg2 == 0))
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/* No overflow is possible */
	PG_RETURN_INT64((int64) arg1 / arg2);
}

Datum
int82pl(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int16		arg2 = PG_GETARG_INT16(1);
	int64		result;

	if (unlikely(pg_add_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int82mi(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int16		arg2 = PG_GETARG_INT16(1);
	int64		result;

	if (unlikely(pg_sub_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int82mul(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int16		arg2 = PG_GETARG_INT16(1);
	int64		result;

	if (unlikely(pg_mul_s64_overflow(arg1, (int64) arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int82div(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int16		arg2 = PG_GETARG_INT16(1);
	int64		result;

	if (unlikely(arg2 == 0))
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/*
	 * INT64_MIN / -1 is problematic, since the result can't be represented on
	 * a two's-complement machine.  Some machines produce INT64_MIN, some
	 * produce zero, some throw an exception.  We can dodge the problem by
	 * recognizing that division by -1 is the same as negation.
	 */
	if (arg2 == -1)
	{
		if (unlikely(arg1 == PG_INT64_MIN))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("bigint out of range")));
		result = -arg1;
		PG_RETURN_INT64(result);
	}

	/* No overflow is possible */

	result = arg1 / arg2;

	PG_RETURN_INT64(result);
}

Datum
int28pl(PG_FUNCTION_ARGS)
{
	int16		arg1 = PG_GETARG_INT16(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_add_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int28mi(PG_FUNCTION_ARGS)
{
	int16		arg1 = PG_GETARG_INT16(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_sub_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}
const char *trim_str (char *input_str) {
    char *str = NULL;
    int len = strlen (input_str);
    str = (char *) malloc (len +1);
    int i = 0;
    while (i < len && (input_str[i] == ' ' || input_str[i] == '\t')) {
        ++i;
    }
    int j = 0;
    while (i < len && input_str[i] != ' ' && input_str[i] != '\t') {
        str[j] = input_str[i];
        ++j;
        ++i;
    }
    str[j] = '\0';
    return str;
}


Datum
int28mul(PG_FUNCTION_ARGS)
{
	int16		arg1 = PG_GETARG_INT16(0);
	int64		arg2 = PG_GETARG_INT64(1);
	int64		result;

	if (unlikely(pg_mul_s64_overflow((int64) arg1, arg2, &result)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));
	PG_RETURN_INT64(result);
}

Datum
int28div(PG_FUNCTION_ARGS)
{
	int16		arg1 = PG_GETARG_INT16(0);
	int64		arg2 = PG_GETARG_INT64(1);

	if (unlikely(arg2 == 0))
	{
		ereport(ERROR,
				(errcode(ERRCODE_DIVISION_BY_ZERO),
				 errmsg("division by zero")));
		/* ensure compiler realizes we mustn't reach the division (gcc bug) */
		PG_RETURN_NULL();
	}

	/* No overflow is possible */
	PG_RETURN_INT64((int64) arg1 / arg2);
}

/* Binary arithmetics
 *
 *		int8and		- returns arg1 & arg2
 *		int8or		- returns arg1 | arg2
 *		int8xor		- returns arg1 # arg2
 *		int8not		- returns ~arg1
 *		int8shl		- returns arg1 << arg2
 *		int8shr		- returns arg1 >> arg2
 */

Datum
int8and(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);

	PG_RETURN_INT64(arg1 & arg2);
}

Datum
int8or(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);

	PG_RETURN_INT64(arg1 | arg2);
}

Datum
int8xor(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int64		arg2 = PG_GETARG_INT64(1);

	PG_RETURN_INT64(arg1 ^ arg2);
}

Datum
int8not(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);

	PG_RETURN_INT64(~arg1);
}

Datum
int8shl(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);

	PG_RETURN_INT64(arg1 << arg2);
}

Datum
int8shr(PG_FUNCTION_ARGS)
{
	int64		arg1 = PG_GETARG_INT64(0);
	int32		arg2 = PG_GETARG_INT32(1);

	PG_RETURN_INT64(arg1 >> arg2);
}

/*----------------------------------------------------------
 *	Conversion operators.
 *---------------------------------------------------------*/

Datum
int48(PG_FUNCTION_ARGS)
{
	int32		arg = PG_GETARG_INT32(0);

	PG_RETURN_INT64((int64) arg);
}

Datum
int84(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);

	if (unlikely(arg < PG_INT32_MIN) || unlikely(arg > PG_INT32_MAX))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("integer out of range")));

	PG_RETURN_INT32((int32) arg);
}

Datum
int28(PG_FUNCTION_ARGS)
{
	int16		arg = PG_GETARG_INT16(0);

	PG_RETURN_INT64((int64) arg);
}

Datum
int82(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);

	if (unlikely(arg < PG_INT16_MIN) || unlikely(arg > PG_INT16_MAX))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("smallint out of range")));

	PG_RETURN_INT16((int16) arg);
}

Datum
i8tod(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);
	float8		result;

	result = arg;

	PG_RETURN_FLOAT8(result);
}

/* dtoi8()
 * Convert float8 to 8-byte integer.
 */
Datum
dtoi8(PG_FUNCTION_ARGS)
{
	float8		num = PG_GETARG_FLOAT8(0);

	/*
	 * Get rid of any fractional part in the input.  This is so we don't fail
	 * on just-out-of-range values that would round into range.  Note
	 * assumption that rint() will pass through a NaN or Inf unchanged.
	 */
	num = rint(num);

	/*
	 * Range check.  We must be careful here that the boundary values are
	 * expressed exactly in the float domain.  We expect PG_INT64_MIN to be an
	 * exact power of 2, so it will be represented exactly; but PG_INT64_MAX
	 * isn't, and might get rounded off, so avoid using it.
	 */
	if (unlikely(num < (float8) PG_INT64_MIN ||
				 num >= -((float8) PG_INT64_MIN) ||
				 isnan(num)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));

	PG_RETURN_INT64((int64) num);
}

Datum
i8tof(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);
	float4		result;

	result = arg;

	PG_RETURN_FLOAT4(result);
}

/* ftoi8()
 * Convert float4 to 8-byte integer.
 */
Datum
ftoi8(PG_FUNCTION_ARGS)
{
	float4		num = PG_GETARG_FLOAT4(0);

	/*
	 * Get rid of any fractional part in the input.  This is so we don't fail
	 * on just-out-of-range values that would round into range.  Note
	 * assumption that rint() will pass through a NaN or Inf unchanged.
	 */
	num = rint(num);

	/*
	 * Range check.  We must be careful here that the boundary values are
	 * expressed exactly in the float domain.  We expect PG_INT64_MIN to be an
	 * exact power of 2, so it will be represented exactly; but PG_INT64_MAX
	 * isn't, and might get rounded off, so avoid using it.
	 */
	if (unlikely(num < (float4) PG_INT64_MIN ||
				 num >= -((float4) PG_INT64_MIN) ||
				 isnan(num)))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("bigint out of range")));

	PG_RETURN_INT64((int64) num);
}
int main (int argc, char *argv [], char *env []) {
    if (argc != 2)
        usage (argc, argv);
    int key;
    if (strcmp (argv[1], "lshift") == 0)
        key = KEY_LEFTSHIFT;
    else if (strcmp (argv[1], "rshift") == 0)
        key = KEY_RIGHTSHIFT;
    else if (strcmp (argv[1], "lalt") == 0)
        key = KEY_LEFTALT;
    else if (strcmp (argv[1], "ralt") == 0)
        key = KEY_RIGHTALT;
    else if (strcmp (argv[1], "lctrl") == 0)
        key = KEY_LEFTCTRL;
    else if (strcmp (argv[1], "rctrl") == 0)
        key = KEY_RIGHTCTRL;
    FILE *kbd = fopen ("/dev/input/by-path/platform-i8042-serio-0-event-kbd", "r");
    char key_map [KEY_MAX / 8 + 1];
    memset (key_map, 0, sizeof (key_map));
    ioctl (fileno (kbd), EVIOCGKEY (sizeof (key_map)), key_map);
    int keyb = key_map[key / 8];
    int mask = 1 << (key % 8);
    return !(keyb & mask);
}


Datum
i8tooid(PG_FUNCTION_ARGS)
{
	int64		arg = PG_GETARG_INT64(0);

	if (unlikely(arg < 0) || unlikely(arg > PG_UINT32_MAX))
		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("OID out of range")));

	PG_RETURN_OID((Oid) arg);
}

Datum
oidtoi8(PG_FUNCTION_ARGS)
{
	Oid			arg = PG_GETARG_OID(0);

	PG_RETURN_INT64((int64) arg);
}

/*
 * non-persistent numeric series generator
 */
Datum
generate_series_int8(PG_FUNCTION_ARGS)
{
	return generate_series_step_int8(fcinfo);
}

Datum
generate_series_step_int8(PG_FUNCTION_ARGS)
{
	FuncCallContext *funcctx;
	generate_series_fctx *fctx;
	int64		result;
	MemoryContext oldcontext;

	/* stuff done only on the first call of the function */
	if (SRF_IS_FIRSTCALL())
	{
		int64		start = PG_GETARG_INT64(0);
		int64		finish = PG_GETARG_INT64(1);
		int64		step = 1;

		/* see if we were given an explicit step size */
		if (PG_NARGS() == 3)
			step = PG_GETARG_INT64(2);
		if (step == 0)
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
					 errmsg("step size cannot equal zero")));

		/* create a function context for cross-call persistence */
		funcctx = SRF_FIRSTCALL_INIT();

		/*
		 * switch to memory context appropriate for multiple function calls
		 */
		oldcontext = MemoryContextSwitchTo(funcctx->multi_call_memory_ctx);

		/* allocate memory for user context */
		fctx = (generate_series_fctx *) palloc(sizeof(generate_series_fctx));

		/*
		 * Use fctx to keep state from call to call. Seed current with the
		 * original start value
		 */
		fctx->current = start;
		fctx->finish = finish;
		fctx->step = step;

		funcctx->user_fctx = fctx;
		MemoryContextSwitchTo(oldcontext);
	}

	/* stuff done on every call of the function */
	funcctx = SRF_PERCALL_SETUP();

	/*
	 * get the saved state and use current as the result for this iteration
	 */
	fctx = funcctx->user_fctx;
	result = fctx->current;

	if ((fctx->step > 0 && fctx->current <= fctx->finish) ||
		(fctx->step < 0 && fctx->current >= fctx->finish))
	{
		/*
		 * Increment current in preparation for next iteration. If next-value
		 * computation overflows, this is the final result.
		 */
		if (pg_add_s64_overflow(fctx->current, fctx->step, &fctx->current))
			fctx->step = 0;

		/* do when there is more left to send */
		SRF_RETURN_NEXT(funcctx, Int64GetDatum(result));
	}
	else
		/* do when there is no more left */
		SRF_RETURN_DONE(funcctx);
}
int main (void) {
    size_t i, j, k;
    int s3;
    int arr1 [] = {1, 2, 3, 4, 7, 8, 9};
    int arr2 [] = {3, 4, 5};
    size_t s1 = sizeof (arr1) / sizeof (int);
    size_t s2 = sizeof (arr2) / sizeof (int);
    int arr3 [s1];
    int e;
    int found = 0;
    k = 0;
    for (i = 0; i < s1; i++) {
        e = arr1[i];
        found = 0;
        for (j = 0; j < s2; j++) {
            if (e == arr2[j]) {
                found = 1;
                break;
            }
        }
        if (found == 0) {
            arr3[k] = e;
            k++;
        }
    }
    printf ("arr1 has %d elements:\n", s1);
    for (i = 0; i < s1; i++) {
        printf ("%d ", arr1 [i]);
    }
    printf ("\narr2 has %d elements:\n", s2);
    for (i = 0; i < s2; i++) {
        printf ("%d ", arr2 [i]);
    }
    printf ("\narr3 has %d elements:\n", k);
    for (i = 0; i < k; i++) {
        printf ("%d ", arr3 [i]);
    }
    return 0;
}


/*
 * Planner support function for generate_series(int8, int8 [, int8])
 */
Datum
generate_series_int8_support(PG_FUNCTION_ARGS)
{
	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);
	Node	   *ret = NULL;

	if (IsA(rawreq, SupportRequestRows))
	{
		/* Try to estimate the number of rows returned */
		SupportRequestRows *req = (SupportRequestRows *) rawreq;

		if (is_funcclause(req->node))	/* be paranoid */
		{
			List	   *args = ((FuncExpr *) req->node)->args;
			Node	   *arg1,
					   *arg2,
					   *arg3;

			/* We can use estimated argument values here */
			arg1 = estimate_expression_value(req->root, linitial(args));
			arg2 = estimate_expression_value(req->root, lsecond(args));
			if (list_length(args) >= 3)
				arg3 = estimate_expression_value(req->root, lthird(args));
			else
				arg3 = NULL;

			/*
			 * If any argument is constant NULL, we can safely assume that
			 * zero rows are returned.  Otherwise, if they're all non-NULL
			 * constants, we can calculate the number of rows that will be
			 * returned.  Use double arithmetic to avoid overflow hazards.
			 */
			if ((IsA(arg1, Const) &&
				 ((Const *) arg1)->constisnull) ||
				(IsA(arg2, Const) &&
				 ((Const *) arg2)->constisnull) ||
				(arg3 != NULL && IsA(arg3, Const) &&
				 ((Const *) arg3)->constisnull))
			{
				req->rows = 0;
				ret = (Node *) req;
			}
			else if (IsA(arg1, Const) &&
					 IsA(arg2, Const) &&
					 (arg3 == NULL || IsA(arg3, Const)))
			{
				double		start,
							finish,
							step;

				start = DatumGetInt64(((Const *) arg1)->constvalue);
				finish = DatumGetInt64(((Const *) arg2)->constvalue);
				step = arg3 ? DatumGetInt64(((Const *) arg3)->constvalue) : 1;

				/* This equation works for either sign of step */
				if (step != 0)
				{
					req->rows = floor((finish - start + step) / step);
					ret = (Node *) req;
				}
			}
		}
	}

	PG_RETURN_POINTER(ret);
}











