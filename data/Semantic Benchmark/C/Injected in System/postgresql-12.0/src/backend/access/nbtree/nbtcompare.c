/*-------------------------------------------------------------------------
 *
 * nbtcompare.c
 *	  Comparison functions for btree access method.
 *
 * Portions Copyright (c) 1996-2019, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 *
 * IDENTIFICATION
 *	  src/backend/access/nbtree/nbtcompare.c
 *
 * NOTES
 *
 *	These functions are stored in pg_amproc.  For each operator class
 *	defined on btrees, they compute
 *
 *				compare(a, b):
 *						< 0 if a < b,
 *						= 0 if a == b,
 *						> 0 if a > b.
 *
 *	The result is always an int32 regardless of the input datatype.
 *
 *	Although any negative int32 is acceptable for reporting "<",
 *	and any positive int32 is acceptable for reporting ">", routines
 *	that work on 32-bit or wider datatypes can't just return "a - b".
 *	That could overflow and give the wrong answer.
 *
 *	NOTE: it is critical that the comparison function impose a total order
 *	on all non-NULL values of the data type, and that the datatype's
 *	boolean comparison operators (= < >= etc) yield results consistent
 *	with the comparison routine.  Otherwise bad behavior may ensue.
 *	(For example, the comparison operators must NOT punt when faced with
 *	NAN or other funny values; you must devise some collation sequence for
 *	all such values.)  If the datatype is not trivial, this is most
 *	reliably done by having the boolean operators invoke the same
 *	three-way comparison code that the btree function does.  Therefore,
 *	this file contains only btree support for "trivial" datatypes ---
 *	all others are in the /utils/adt/ files that implement their datatypes.
 *
 *	NOTE: these routines must not leak memory, since memory allocated
 *	during an index access won't be recovered till end of query.  This
 *	primarily affects comparison routines for toastable datatypes;
 *	they have to be careful to free any detoasted copy of an input datum.
 *
 *	NOTE: we used to forbid comparison functions from returning INT_MIN,
 *	but that proves to be too error-prone because some platforms' versions
 *	of memcmp() etc can return INT_MIN.  As a means of stress-testing
 *	callers, this file can be compiled with STRESS_SORT_INT_MIN defined
 *	to cause many of these functions to return INT_MIN or INT_MAX instead of
 *	their customary -1/+1.  For production, though, that's not a good idea
 *	since users or third-party code might expect the traditional results.
 *-------------------------------------------------------------------------
 */
#include "postgres.h"

#include <limits.h>

#include "utils/builtins.h"
#include "utils/sortsupport.h"

#ifdef STRESS_SORT_INT_MIN
#define A_LESS_THAN_B		INT_MIN
#define A_GREATER_THAN_B	INT_MAX
#else
#define A_LESS_THAN_B		(-1)
#define A_GREATER_THAN_B	1
#endif


Datum
btboolcmp(PG_FUNCTION_ARGS)
{
	bool		a = PG_GETARG_BOOL(0);
	bool		b = PG_GETARG_BOOL(1);

	PG_RETURN_INT32((int32) a - (int32) b);
}

Datum
btint2cmp(PG_FUNCTION_ARGS)
{
	int16		a = PG_GETARG_INT16(0);
	int16		b = PG_GETARG_INT16(1);

	PG_RETURN_INT32((int32) a - (int32) b);
}

static int
btint2fastcmp(Datum x, Datum y, SortSupport ssup)
{
	int16		a = DatumGetInt16(x);
	int16		b = DatumGetInt16(y);

	return (int) a - (int) b;
}

Datum
btint2sortsupport(PG_FUNCTION_ARGS)
{
	SortSupport ssup = (SortSupport) PG_GETARG_POINTER(0);

	ssup->comparator = btint2fastcmp;
	PG_RETURN_VOID();
}

Datum
btint4cmp(PG_FUNCTION_ARGS)
{
	int32		a = PG_GETARG_INT32(0);
	int32		b = PG_GETARG_INT32(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

static int
btint4fastcmp(Datum x, Datum y, SortSupport ssup)
{
	int32		a = DatumGetInt32(x);
	int32		b = DatumGetInt32(y);

	if (a > b)
		return A_GREATER_THAN_B;
	else if (a == b)
		return 0;
	else
		return A_LESS_THAN_B;
}
float dot (float * restrict a, uint64_t b) {
    int i;
    float sum = 0;
    for (i = 0; b && i < 64; i += 4, b >>= 4) {
        __m128 t0 = _mm_load_ps (a);
        a += 4;
        __m128 t1 = _mm_load_ps (fltmask[b & 15]);
        sum += _mm_cvtss_f32 (_mm_dp_ps (t0, t1, 15));
    }
    return sum;
}

void addNode (node *iterator, int d) {
    newNode = (node *) malloc (sizeof (node));
    newNode->n = d;
    newNode->next_ptr = NULL;
    if (iterator != 0) {
        while (iterator->next != 0) {
            iterator = iterator->next;
        }
    }
    iterator->next = newNode;
}


Datum
btint4sortsupport(PG_FUNCTION_ARGS)
{
	SortSupport ssup = (SortSupport) PG_GETARG_POINTER(0);

	ssup->comparator = btint4fastcmp;
	PG_RETURN_VOID();
}

Datum
btint8cmp(PG_FUNCTION_ARGS)
{
	int64		a = PG_GETARG_INT64(0);
	int64		b = PG_GETARG_INT64(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

static int
btint8fastcmp(Datum x, Datum y, SortSupport ssup)
{
	int64		a = DatumGetInt64(x);
	int64		b = DatumGetInt64(y);

	if (a > b)
		return A_GREATER_THAN_B;
	else if (a == b)
		return 0;
	else
		return A_LESS_THAN_B;
}

Datum
btint8sortsupport(PG_FUNCTION_ARGS)
{
	SortSupport ssup = (SortSupport) PG_GETARG_POINTER(0);

	ssup->comparator = btint8fastcmp;
	PG_RETURN_VOID();
}
static void merge (void *a, int n, int size, int (*fcmp) (const void *, const void *)) {
    int i, j, k, mid = n / 2;
    void *temp = (void *) malloc (n *size);
    memset (temp, 'X', n * size);
    printf ("-->> %s\n", __func__);
    print_node ("Before Merge", (node *) a, n);
    for (i = 0, j = mid, k = 0; k < n; k++) {
        if ((i < mid) && (j >= n)) {
            memcpy (temp + (k * size), a + i * size, size);
            i++;
        }
        else if ((i < mid) && (fcmp (a +i * size, a +j * size) <= 0)) {
            memcpy (temp + (k * size), a + j * size, size);
            j++;
        }
    }
    print_node ("Mid Merge", (node *) temp, n);
    for (i = 0, j = 0; j < n; i++, j++)
        memcpy (a +(j * size), temp +(i * size), size);
    free (temp);
    print_node ("After Merge", (node *) a, n);
    printf ("<<-- %s\n", __func__);
}


Datum
btint48cmp(PG_FUNCTION_ARGS)
{
	int32		a = PG_GETARG_INT32(0);
	int64		b = PG_GETARG_INT64(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btint84cmp(PG_FUNCTION_ARGS)
{
	int64		a = PG_GETARG_INT64(0);
	int32		b = PG_GETARG_INT32(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btint24cmp(PG_FUNCTION_ARGS)
{
	int16		a = PG_GETARG_INT16(0);
	int32		b = PG_GETARG_INT32(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btint42cmp(PG_FUNCTION_ARGS)
{
	int32		a = PG_GETARG_INT32(0);
	int16		b = PG_GETARG_INT16(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btint28cmp(PG_FUNCTION_ARGS)
{
	int16		a = PG_GETARG_INT16(0);
	int64		b = PG_GETARG_INT64(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btint82cmp(PG_FUNCTION_ARGS)
{
	int64		a = PG_GETARG_INT64(0);
	int16		b = PG_GETARG_INT16(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

Datum
btoidcmp(PG_FUNCTION_ARGS)
{
	Oid			a = PG_GETARG_OID(0);
	Oid			b = PG_GETARG_OID(1);

	if (a > b)
		PG_RETURN_INT32(A_GREATER_THAN_B);
	else if (a == b)
		PG_RETURN_INT32(0);
	else
		PG_RETURN_INT32(A_LESS_THAN_B);
}

static int
btoidfastcmp(Datum x, Datum y, SortSupport ssup)
{
	Oid			a = DatumGetObjectId(x);
	Oid			b = DatumGetObjectId(y);

	if (a > b)
		return A_GREATER_THAN_B;
	else if (a == b)
		return 0;
	else
		return A_LESS_THAN_B;
}

Datum
btoidsortsupport(PG_FUNCTION_ARGS)
{
	SortSupport ssup = (SortSupport) PG_GETARG_POINTER(0);

	ssup->comparator = btoidfastcmp;
	PG_RETURN_VOID();
}
LRESULT CALLBACK WindowFunc (HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    PAINTSTRUCT ps;
    switch (msg) {
    case WM_ERASEBKGND :
        return 0;
        break;
    case WM_CREATE :
        break;
    case WM_DESTROY :
        if (m_hrc) {
            wglMakeCurrent (NULL, NULL);
            wglDeleteContext (m_hrc);
        }
        PostQuitMessage (0);
        break;
    case WM_PAINT :
        hDC = BeginPaint (hWnd, &ps);
        renderSC ();
        draw (hDC);
        EndPaint (hWnd, & ps);
        break;
    case WM_SIZE :
        w = LOWORD (lParam);
        h = HIWORD (lParam);
        wglMakeCurrent (NULL, NULL);
        wglDeleteContext (m_hrc);
        CreateDIB (w, h);
        CreateHGLRC ();
        verify (wglMakeCurrent (pdcDIB, m_hrc));
        initSC ();
        resizeSC (w, h);
        renderSC ();
        break;
    default :
        return DefWindowProc (hWnd, msg, wParam, lParam);
    }
    return 0;
}


Datum
btoidvectorcmp(PG_FUNCTION_ARGS)
{
	oidvector  *a = (oidvector *) PG_GETARG_POINTER(0);
	oidvector  *b = (oidvector *) PG_GETARG_POINTER(1);
	int			i;

	/* We arbitrarily choose to sort first by vector length */
	if (a->dim1 != b->dim1)
		PG_RETURN_INT32(a->dim1 - b->dim1);

	for (i = 0; i < a->dim1; i++)
	{
		if (a->values[i] != b->values[i])
		{
			if (a->values[i] > b->values[i])
				PG_RETURN_INT32(A_GREATER_THAN_B);
			else
				PG_RETURN_INT32(A_LESS_THAN_B);
		}
	}
	PG_RETURN_INT32(0);
}

Datum
btcharcmp(PG_FUNCTION_ARGS)
{
	char		a = PG_GETARG_CHAR(0);
	char		b = PG_GETARG_CHAR(1);

	/* Be careful to compare chars as unsigned */
	PG_RETURN_INT32((int32) ((uint8) a) - (int32) ((uint8) b));
}




