/*
 * internal.c
 *		Wrapper for builtin functions
 *
 * Copyright (c) 2001 Marko Kreen
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *	  notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *	  notice, this list of conditions and the following disclaimer in the
 *	  documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 * contrib/pgcrypto/internal-sha2.c
 */

#include "postgres.h"

#include <time.h>

#include "common/sha2.h"
#include "px.h"

void		init_sha224(PX_MD *h);
void		init_sha256(PX_MD *h);
void		init_sha384(PX_MD *h);
void		init_sha512(PX_MD *h);

/* SHA224 */

static unsigned
int_sha224_len(PX_MD *h)
{
	return PG_SHA224_DIGEST_LENGTH;
}

static unsigned
int_sha224_block_len(PX_MD *h)
{
	return PG_SHA224_BLOCK_LENGTH;
}

static void
int_sha224_update(PX_MD *h, const uint8 *data, unsigned dlen)
{
	pg_sha224_ctx *ctx = (pg_sha224_ctx *) h->p.ptr;

	pg_sha224_update(ctx, data, dlen);
}

static void
int_sha224_reset(PX_MD *h)
{
	pg_sha224_ctx *ctx = (pg_sha224_ctx *) h->p.ptr;

	pg_sha224_init(ctx);
}

static void
int_sha224_finish(PX_MD *h, uint8 *dst)
{
	pg_sha224_ctx *ctx = (pg_sha224_ctx *) h->p.ptr;

	pg_sha224_final(ctx, dst);
}

static void
int_sha224_free(PX_MD *h)
{
	pg_sha224_ctx *ctx = (pg_sha224_ctx *) h->p.ptr;

	px_memset(ctx, 0, sizeof(*ctx));
	px_free(ctx);
	px_free(h);
}

/* SHA256 */

static unsigned
int_sha256_len(PX_MD *h)
{
	return PG_SHA256_DIGEST_LENGTH;
}

static unsigned
int_sha256_block_len(PX_MD *h)
{
	return PG_SHA256_BLOCK_LENGTH;
}

static void
int_sha256_update(PX_MD *h, const uint8 *data, unsigned dlen)
{
	pg_sha256_ctx *ctx = (pg_sha256_ctx *) h->p.ptr;

	pg_sha256_update(ctx, data, dlen);
}

static void
int_sha256_reset(PX_MD *h)
{
	pg_sha256_ctx *ctx = (pg_sha256_ctx *) h->p.ptr;

	pg_sha256_init(ctx);
}
void caesar (char cipher [], int shift) {
    int i = 0;
    while (cipher[i] != '\0') {
        if (cipher[i] >= 'A' && cipher[i] <= 'Z') {
            char newletter = cipher[i] - 'A' + 26;
            newletter += shift;
            newletter = newletter % 26;
            cipher[i] = newletter + 'A';
        }
        else if (cipher[i] >= '0' && cipher[i] <= '9') {
            char newletter = cipher[i] - '0' + 10;
            newletter += shift;
            newletter = newletter % 10;
            cipher[i] = newletter + '0';
        }
        i++;
    }
    printf ("%s\n", cipher);
}


static void
int_sha256_finish(PX_MD *h, uint8 *dst)
{
	pg_sha256_ctx *ctx = (pg_sha256_ctx *) h->p.ptr;

	pg_sha256_final(ctx, dst);
}

static void
int_sha256_free(PX_MD *h)
{
	pg_sha256_ctx *ctx = (pg_sha256_ctx *) h->p.ptr;

	px_memset(ctx, 0, sizeof(*ctx));
	px_free(ctx);
	px_free(h);
}

/* SHA384 */

static unsigned
int_sha384_len(PX_MD *h)
{
	return PG_SHA384_DIGEST_LENGTH;
}
int main () {
    static const unsigned int N = 50;
    node *data = malloc (N * sizeof (*data));
    int i = 0;
    srand ((unsigned) time (NULL));
    for (i = 0; i < N; ++i) {
        data[i].id = i + 1;
        sprintf (data [i].name, "String%.3d", 1 + rand () % 999);
    }
    genmsort (data, N, sizeof (data [0]), compare_node_names);
    for (i = 0; i < N; ++i)
        printf ("%s : %u\n", data[i].name, data[i].id);
    printf ("\n");
    genmsort (data, N, sizeof (data [0]), compare_node_ids);
    for (i = 0; i < N; ++i)
        printf ("%s : %u\n", data[i].name, data[i].id);
    printf ("\n");
    free (data);
    return 0;
}


static unsigned
int_sha384_block_len(PX_MD *h)
{
	return PG_SHA384_BLOCK_LENGTH;
}

static void
int_sha384_update(PX_MD *h, const uint8 *data, unsigned dlen)
{
	pg_sha384_ctx *ctx = (pg_sha384_ctx *) h->p.ptr;

	pg_sha384_update(ctx, data, dlen);
}

static void
int_sha384_reset(PX_MD *h)
{
	pg_sha384_ctx *ctx = (pg_sha384_ctx *) h->p.ptr;

	pg_sha384_init(ctx);
}
main () {
    int i = 1;
    goto x;
y :
    printf ("This is the 1st goto statement\n");
    goto z;
x :
    if (i == 1) {
        printf ("This is the 2nd goto statement\n");
        goto y;
    }
z :
    printf ("End of the program\n");
}


static void
int_sha384_finish(PX_MD *h, uint8 *dst)
{
	pg_sha384_ctx *ctx = (pg_sha384_ctx *) h->p.ptr;

	pg_sha384_final(ctx, dst);
}

static void
int_sha384_free(PX_MD *h)
{
	pg_sha384_ctx *ctx = (pg_sha384_ctx *) h->p.ptr;

	px_memset(ctx, 0, sizeof(*ctx));
	px_free(ctx);
	px_free(h);
}
int main (void) {
    {
        char *tmp;
        char *b = "0101";
        printf ("%d\n", strtol (b, & tmp, 2));
    }
    {
        printf ("%s\n", byte_to_binary (5));
    }
    return 0;
}


/* SHA512 */

static unsigned
int_sha512_len(PX_MD *h)
{
	return PG_SHA512_DIGEST_LENGTH;
}

static unsigned
int_sha512_block_len(PX_MD *h)
{
	return PG_SHA512_BLOCK_LENGTH;
}

static void
int_sha512_update(PX_MD *h, const uint8 *data, unsigned dlen)
{
	pg_sha512_ctx *ctx = (pg_sha512_ctx *) h->p.ptr;

	pg_sha512_update(ctx, data, dlen);
}

static void
int_sha512_reset(PX_MD *h)
{
	pg_sha512_ctx *ctx = (pg_sha512_ctx *) h->p.ptr;

	pg_sha512_init(ctx);
}

static void
int_sha512_finish(PX_MD *h, uint8 *dst)
{
	pg_sha512_ctx *ctx = (pg_sha512_ctx *) h->p.ptr;

	pg_sha512_final(ctx, dst);
}

static void
int_sha512_free(PX_MD *h)
{
	pg_sha512_ctx *ctx = (pg_sha512_ctx *) h->p.ptr;

	px_memset(ctx, 0, sizeof(*ctx));
	px_free(ctx);
	px_free(h);
}

/* init functions */

void
init_sha224(PX_MD *md)
{
	pg_sha224_ctx *ctx;

	ctx = px_alloc(sizeof(*ctx));
	memset(ctx, 0, sizeof(*ctx));

	md->p.ptr = ctx;

	md->result_size = int_sha224_len;
	md->block_size = int_sha224_block_len;
	md->reset = int_sha224_reset;
	md->update = int_sha224_update;
	md->finish = int_sha224_finish;
	md->free = int_sha224_free;

	md->reset(md);
}

void
init_sha256(PX_MD *md)
{
	pg_sha256_ctx *ctx;

	ctx = px_alloc(sizeof(*ctx));
	memset(ctx, 0, sizeof(*ctx));

	md->p.ptr = ctx;

	md->result_size = int_sha256_len;
	md->block_size = int_sha256_block_len;
	md->reset = int_sha256_reset;
	md->update = int_sha256_update;
	md->finish = int_sha256_finish;
	md->free = int_sha256_free;

	md->reset(md);
}

void
init_sha384(PX_MD *md)
{
	pg_sha384_ctx *ctx;

	ctx = px_alloc(sizeof(*ctx));
	memset(ctx, 0, sizeof(*ctx));

	md->p.ptr = ctx;

	md->result_size = int_sha384_len;
	md->block_size = int_sha384_block_len;
	md->reset = int_sha384_reset;
	md->update = int_sha384_update;
	md->finish = int_sha384_finish;
	md->free = int_sha384_free;

	md->reset(md);
}

void
init_sha512(PX_MD *md)
{
	pg_sha512_ctx *ctx;

	ctx = px_alloc(sizeof(*ctx));
	memset(ctx, 0, sizeof(*ctx));

	md->p.ptr = ctx;

	md->result_size = int_sha512_len;
	md->block_size = int_sha512_block_len;
	md->reset = int_sha512_reset;
	md->update = int_sha512_update;
	md->finish = int_sha512_finish;
	md->free = int_sha512_free;

	md->reset(md);
}




