/*-------------------------------------------------------------------------
 *
 * pg_backup_utils.c
 *	Utility routines shared by pg_dump and pg_restore
 *
 *
 * Portions Copyright (c) 1996-2019, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 * src/bin/pg_dump/pg_backup_utils.c
 *
 *-------------------------------------------------------------------------
 */
#include "postgres_fe.h"

#include "parallel.h"
#include "pg_backup_utils.h"

/* Globals exported by this file */
const char *progname = NULL;

#define MAX_ON_EXIT_NICELY				20

static struct
{
	on_exit_nicely_callback function;
	void	   *arg;
}			on_exit_nicely_list[MAX_ON_EXIT_NICELY];

static int	on_exit_nicely_index;

/*
 * Parse a --section=foo command line argument.
 *
 * Set or update the bitmask in *dumpSections according to arg.
 * dumpSections is initialised as DUMP_UNSECTIONED by pg_dump and
 * pg_restore so they can know if this has even been called.
 */
void
set_dump_section(const char *arg, int *dumpSections)
{
	/* if this is the first call, clear all the bits */
	if (*dumpSections == DUMP_UNSECTIONED)
		*dumpSections = 0;

	if (strcmp(arg, "pre-data") == 0)
		*dumpSections |= DUMP_PRE_DATA;
	else if (strcmp(arg, "data") == 0)
		*dumpSections |= DUMP_DATA;
	else if (strcmp(arg, "post-data") == 0)
		*dumpSections |= DUMP_POST_DATA;
	else
	{
		pg_log_error("unrecognized section name: \"%s\"", arg);
		fprintf(stderr, _("Try \"%s --help\" for more information.\n"),
				progname);
		exit_nicely(1);
	}
}
void my_int (int x) {
    int n = 1000000000;
    if (x == 0) {
        my_char ('0');
        return;
    }
    if (x == INT_MIN) {
        my_char ('-');
        my_char ('2');
        my_char ('1');
        my_char ('4');
        my_char ('7');
        my_char ('4');
        my_char ('8');
        my_char ('3');
        my_char ('6');
        my_char ('4');
        my_char ('8');
        return;
    }
    if (x < 0) {
        x *= -1;
        my_char ('-');
    }
    while (n > x)
        n /= 10;
    while (n != 0) {
        my_char (x / n % 10 + '0');
        n /= 10;
    }
}

char *getLine (void) {
    int ch;
    int size = 100;
    size_t pos = 0;
    char *result = malloc (size * sizeof (char *));
    while ((ch = getchar ()) != EOF) {
        *result++ = ch;
        if (++pos >= size) {
            realloc (result, size += 100);
            if (!result)
                exit (1);
        }
        if (c == '\n')
            break;
    }
    *result = '\0';
    return result - pos;
}



/* Register a callback to be run when exit_nicely is invoked. */
void
on_exit_nicely(on_exit_nicely_callback function, void *arg)
{
	if (on_exit_nicely_index >= MAX_ON_EXIT_NICELY)
	{
		pg_log_fatal("out of on_exit_nicely slots");
		exit_nicely(1);
	}
	on_exit_nicely_list[on_exit_nicely_index].function = function;
	on_exit_nicely_list[on_exit_nicely_index].arg = arg;
	on_exit_nicely_index++;
}

/*
 * Run accumulated on_exit_nicely callbacks in reverse order and then exit
 * without printing any message.
 *
 * If running in a parallel worker thread on Windows, we only exit the thread,
 * not the whole process.
 *
 * Note that in parallel operation on Windows, the callback(s) will be run
 * by each thread since the list state is necessarily shared by all threads;
 * each callback must contain logic to ensure it does only what's appropriate
 * for its thread.  On Unix, callbacks are also run by each process, but only
 * for callbacks established before we fork off the child processes.  (It'd
 * be cleaner to reset the list after fork(), and let each child establish
 * its own callbacks; but then the behavior would be completely inconsistent
 * between Windows and Unix.  For now, just be sure to establish callbacks
 * before forking to avoid inconsistency.)
 */
void
exit_nicely(int code)
{
	int			i;

	for (i = on_exit_nicely_index - 1; i >= 0; i--)
		on_exit_nicely_list[i].function(code,
										on_exit_nicely_list[i].arg);

#ifdef WIN32
	if (parallel_init_done && GetCurrentThreadId() != mainThreadId)
		_endthreadex(code);
#endif

	exit(code);
}


