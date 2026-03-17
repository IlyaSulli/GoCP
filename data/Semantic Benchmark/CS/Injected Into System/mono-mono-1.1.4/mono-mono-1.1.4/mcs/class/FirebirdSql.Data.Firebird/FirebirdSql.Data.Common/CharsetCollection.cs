/*
 *  Firebird ADO.NET Data provider for .NET and Mono 
 * 
 *     The contents of this file are subject to the Initial 
 *     Developer's Public License Version 1.0 (the "License"); 
 *     you may not use this file except in compliance with the 
 *     License. You may obtain a copy of the License at 
 *     http://www.firebirdsql.org/index.php?op=doc&id=idpl
 *
 *     Software distributed under the License is distributed on 
 *     an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either 
 *     express or implied.  See the License for the specific 
 *     language governing rights and limitations under the License.
 * 
 *  Copyright (c) 2002, 2004 Carlos Guzman Alvarez
 *  All Rights Reserved.
 */

using System;
using System.Text;
using System.Collections;

namespace FirebirdSql.Data.Common
{
	internal sealed class CharsetCollection : CollectionBase
	{
		#region Indexers

		public Charset this[int index]
		{
			get { return (Charset)this.List[index]; }
		}

		public Charset this[string name]
		{
			get { return (Charset)this[this.IndexOf(name)]; }
		}

		#endregion

		#region Methods

		public int IndexOf(int id)
		{
			int index = 0;

			foreach (Charset item in this)
			{
				if (item.ID == id)
				{
					return index;
				}
				index++;
			}

			return -1;
		}
public static void Main () {
    Tuple < string, DateTime, int, DateTime, int > [] cities = {Tuple.Create ("Los Angeles", new DateTime (1940, 1, 1), 1504277, new DateTime (1950, 1, 1), 1970358), Tuple.Create ("New York", new DateTime (1940, 1, 1), 7454995, new DateTime (1950, 1, 1), 7891957), Tuple.Create ("Chicago", new DateTime (1940, 1, 1), 3396808, new DateTime (1950, 1, 1), 3620962), Tuple.Create ("Detroit", new DateTime (1940, 1, 1), 1623452, new DateTime (1950, 1, 1), 1849568)};
    string header = String.Format ("{0,-12}{1,8}{2,12}{1,8}{2,12}{3,14}\n", "City", "Year", "Population", "Change (%)");
    Console.WriteLine (header);
    string output;
    foreach (var city in cities) {
        output = String.Format ("{0,-12}{1,8:yyyy}{2,12:N0}{3,8:yyyy}{4,12:N0}{5,14:P1}", city.Item1, city.Item2, city.Item3, city.Item4, city.Item5, (city.Item5 - city.Item3) / (double) city.Item3);
        Console.WriteLine (output);
    }
}


		public int IndexOf(string name)
		{
			int index = 0;

			foreach (Charset item in this)
			{
				if (GlobalizationHelper.CultureAwareCompare(item.Name, name))
				{
					return index;
				}
				index++;
			}

			return -1;
		}

		internal Charset Add(
			int		id,
			string	charset,
			int		bytesPerCharacter,
			string	systemCharset)
		{
			Charset charSet = new Charset(
				id,
				charset,
				bytesPerCharacter,
				systemCharset);

			return this.Add(charSet);
		}

		internal Charset Add(Charset charset)
		{
			this.List.Add(charset);

			return charset;
		}

		#endregion
	}
}

