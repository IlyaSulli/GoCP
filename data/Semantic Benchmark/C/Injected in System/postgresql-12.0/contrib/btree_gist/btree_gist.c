/*
 * contrib/btree_gist/btree_gist.c
 */
#include "postgres.h"

#include "btree_gist.h"

PG_MODULE_MAGIC;

PG_FUNCTION_INFO_V1(gbt_decompress);
PG_FUNCTION_INFO_V1(gbtreekey_in);
PG_FUNCTION_INFO_V1(gbtreekey_out);

/**************************************************
 * In/Out for keys
 **************************************************/


Datum
gbtreekey_in(PG_FUNCTION_ARGS)
{
	ereport(ERROR,
			(errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
			 errmsg("<datatype>key_in() not implemented")));

	PG_RETURN_POINTER(NULL);
}

#include "btree_utils_var.h"
#include "utils/builtins.h"
Datum
gbtreekey_out(PG_FUNCTION_ARGS)
{
	ereport(ERROR,
			(errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
			 errmsg("<datatype>key_out() not implemented")));
	PG_RETURN_POINTER(NULL);
}


/*
** GiST DeCompress methods
** do not do anything.
*/
Datum
gbt_decompress(PG_FUNCTION_ARGS)
{
	PG_RETURN_POINTER(PG_GETARG_POINTER(0));
}
int main () {
    char ch = 'b';
    char alp [26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    string enc [26] = {"00", "01", "02"};
    map < char, string > valueDecoderMap;
    for (int i = 0; i < (sizeof (alp)); i++) {
        valueDecoderMap[alp[i]] = enc[i];
    }
    map < char, string > : : iterator mapIterator;
    mapIterator = valueDecoderMap.find (ch);
    if (mapIterator != valueDecoderMap.end ()) {
        cout << "Key = " << mapIterator->first << " Value = " << mapIterator->second << endl;
    }
    else {
        cout << "No encoding present for " << ch << endl;
    }
    return 0;
}


