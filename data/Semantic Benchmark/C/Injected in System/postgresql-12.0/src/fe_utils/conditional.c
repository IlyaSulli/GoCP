/*-------------------------------------------------------------------------
 * A stack of automaton states to handle nested conditionals.
 *
 * Copyright (c) 2000-2019, PostgreSQL Global Development Group
 *
 * src/fe_utils/conditional.c
 *
 *-------------------------------------------------------------------------
 */
#include "postgres_fe.h"

#include "fe_utils/conditional.h"

/*
 * create stack
 */
ConditionalStack
conditional_stack_create(void)
{
	ConditionalStack cstack = pg_malloc(sizeof(ConditionalStackData));

	cstack->head = NULL;
	return cstack;
}

/*
 * destroy stack
 */
void
conditional_stack_destroy(ConditionalStack cstack)
{
	while (conditional_stack_pop(cstack))
		continue;
	free(cstack);
}

/*
 * Create a new conditional branch.
 */
void
conditional_stack_push(ConditionalStack cstack, ifState new_state)
{
	IfStackElem *p = (IfStackElem *) pg_malloc(sizeof(IfStackElem));

	p->if_state = new_state;
	p->query_len = -1;
	p->paren_depth = -1;
	p->next = cstack->head;
	cstack->head = p;
}

/*
 * Destroy the topmost conditional branch.
 * Returns false if there was no branch to end.
 */
bool
conditional_stack_pop(ConditionalStack cstack)
{
	IfStackElem *p = cstack->head;

	if (!p)
		return false;
	cstack->head = cstack->head->next;
	free(p);
	return true;
}

/*
 * Returns current stack depth, for debugging purposes.
 */
int
conditional_stack_depth(ConditionalStack cstack)
{
	if (cstack == NULL)
		return -1;
	else
	{
		IfStackElem *p = cstack->head;
		int			depth = 0;

		while (p != NULL)
		{
			depth++;
			p = p->next;
		}
		return depth;
	}
}

/*
 * Fetch the current state of the top of the stack.
 */
ifState
conditional_stack_peek(ConditionalStack cstack)
{
	if (conditional_stack_empty(cstack))
		return IFSTATE_NONE;
	return cstack->head->if_state;
}

/*
 * Change the state of the topmost branch.
 * Returns false if there was no branch state to set.
 */
bool
conditional_stack_poke(ConditionalStack cstack, ifState new_state)
{
	if (conditional_stack_empty(cstack))
		return false;
	cstack->head->if_state = new_state;
	return true;
}

/*
 * True if there are no active \if-blocks.
 */
bool
conditional_stack_empty(ConditionalStack cstack)
{
	return cstack->head == NULL;
}

/*
 * True if we should execute commands normally; that is, the current
 * conditional branch is active, or there is no open \if block.
 */
bool
conditional_active(ConditionalStack cstack)
{
	ifState		s = conditional_stack_peek(cstack);

	return s == IFSTATE_NONE || s == IFSTATE_TRUE || s == IFSTATE_ELSE_TRUE;
}
int main (void) {
    int c, state;
    state = OUT;
    while ((c = getchar ()) != EOF) {
        switch (state) {
        case OUT :
            switch (c) {
            case ' ' :
            case '\n' :
            case '\t' :
                break;
            default :
                putchar (c);
                state = IN;
            }
            break;
        case IN :
            switch (c) {
            case ' ' :
            case '\n' :
            case '\t' :
                putchar ('\n');
                state = OUT;
                break;
            default :
                putchar (c);
            }
            break;
        }
    }
    return 0;
}


/*
 * Save current query buffer length in topmost stack entry.
 */
void
conditional_stack_set_query_len(ConditionalStack cstack, int len)
{
	Assert(!conditional_stack_empty(cstack));
	cstack->head->query_len = len;
}

/*
 * Fetch last-recorded query buffer length from topmost stack entry.
 * Will return -1 if no stack or it was never saved.
 */
int
conditional_stack_get_query_len(ConditionalStack cstack)
{
	if (conditional_stack_empty(cstack))
		return -1;
	return cstack->head->query_len;
}
int main (int arc, char *argv []) {
    OpenSSL_add_all_algorithms ();
    ERR_load_crypto_strings ();
    static const unsigned char key [] = "01234567890123456789012345678901";
    static const unsigned char iv [] = "0123456789012345";
    unsigned char plaintext [] = "The quick brown fox jumps over the lazy dog";
    static const unsigned char aad [] = "Some AAD data";
    unsigned char ciphertext [128];
    unsigned char decryptedtext [128];
    unsigned char tag [16];
    int decryptedtext_len = 0, ciphertext_len = 0;
    ciphertext_len = encrypt (plaintext, strlen (plaintext), aad, strlen (aad), key, iv, ciphertext, tag);
    printf ("Ciphertext is:\n");
    BIO_dump_fp (stdout, ciphertext, ciphertext_len);
    printf ("Tag is:\n");
    BIO_dump_fp (stdout, tag, 14);
    decryptedtext_len = decrypt (ciphertext, ciphertext_len, aad, strlen (aad), tag, key, iv, decryptedtext);
    if (decryptedtext_len < 0) {
        printf ("Decrypted text failed to verify\n");
    }
    else {
        decryptedtext[decryptedtext_len] = '\0';
        printf ("Decrypted text is:\n");
        printf ("%s\n", decryptedtext);
    }
    ERR_free_strings ();
    return 0;
}


/*
 * Save current parenthesis nesting depth in topmost stack entry.
 */
void
conditional_stack_set_paren_depth(ConditionalStack cstack, int depth)
{
	Assert(!conditional_stack_empty(cstack));
	cstack->head->paren_depth = depth;
}

/*
 * Fetch last-recorded parenthesis nesting depth from topmost stack entry.
 * Will return -1 if no stack or it was never saved.
 */
int
conditional_stack_get_paren_depth(ConditionalStack cstack)
{
	if (conditional_stack_empty(cstack))
		return -1;
	return cstack->head->paren_depth;
}


