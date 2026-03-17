// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to
// permit persons to whom the Software is furnished to do so, subject to
// the following conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
// OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//
// Copyright (c) 2004-2005 Novell, Inc.
//
// Authors:
//	Jonathan Chambers (jonathan.chambers@ansys.com)
//

// COMPLETE

using System;
using System.Collections;

namespace System.Windows.Forms
{
	public class GridItemCollection : IEnumerable
	{
		#region	Local Variables
		private System.Collections.SortedList list;
		#endregion	// Local Variables

		#region Public Static Fields
		public static GridItemCollection Empty = new GridItemCollection();
		#endregion	// Public Static Fields

		#region	Constructors
		internal GridItemCollection()
		{
			list = new SortedList();
		}
		#endregion	// Constructors

		#region Internal Properties and Methods
		internal void Add(string key, GridItem grid_item)
		{
			list.Add(key,grid_item);
		}
static void Main (string [] args) {
    try {
        Rethrower ();
    }
    catch (Exception ex) {
        Console.Write (ex.ToString ());
    }
    Console.ReadKey ();
}

		#endregion	// Internal Properties and Methods

		#region	Public Instance Properties
		public int Count
		{
			get {
				return list.Count;
			}
		}

		public GridItem this [int index] 
		{
			get {
				if (index>=list.Count) {
					throw new ArgumentOutOfRangeException("index");
				}
				return (GridItem)list.GetByIndex(index);
			}
		}

		public GridItem this [string key] 
		{
			get {
				return (GridItem)list[key];
			}
		}
		#endregion	// Public Instance Properties

		#region IEnumerable Members
		public IEnumerator GetEnumerator()
		{
			return list.GetEnumerator();
		}
static int GetPlayers () {
    int players = 0;
    Console.Write ("How many people are playing?");
    try {
        players = Convert.ToInt16 (Console.ReadLine ());
    }
    catch (Exception e) {
        Console.Write (e.Message + "\n" + "----------");
        return GetPlayers ();
    }
    return players;
}

		#endregion
	}
}


