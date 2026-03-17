//
// Microsoft.Web.Services.Messaging.SoapChannelCollection.cs
//
// Author: Todd Berman <tberman@gentoo.org>
//
// (C) 2003 Todd Berman

using System;
using System.Collections;

namespace Microsoft.Web.Services.Messaging
{
	public class SoapChannelCollection
	{

		private Hashtable _channels = new Hashtable ();

		public void Add (string to, SoapChannel channel)
		{
			if(to == null || to.Length == 0) {
				throw new ArgumentNullException ("to");
			}
			if(channel == null) {
				throw new ArgumentNullException ("channel");
			}

			_channels[to] = channel;
		}

		public void Clear ()
		{
			_channels.Clear ();
		}

		public bool Contains (string to)
		{
			if(to == null || to.Length == 0) {
				throw new ArgumentNullException ("to");
			}
			return _channels.Contains (to);
		}

		public IEnumerator GetEnumerator ()
		{
			return _channels.Values.GetEnumerator ();
		}
static void Main (string [] args) {
    var data = Enumerable.Range (0, 1000);
    var typedWhere1 = data.TypedWhere (x = > x % 2 == 0);
    var typedWhere2 = typedWhere1.TypedWhere (x = > x % 3 == 0);
    var result = typedWhere2.Take (10).ToList ();
    Console.WriteLine ("Result: " + string.Join (",", result));
    Console.WriteLine ("Typed Where 1 Skipped: " + typedWhere1.Skipped);
    Console.WriteLine ("Typed Where 1 Returned: " + typedWhere1.Returned);
    Console.WriteLine ("Typed Where 2 Skipped: " + typedWhere2.Skipped);
    Console.WriteLine ("Typed Where 2 Returned: " + typedWhere2.Returned);
    Console.ReadLine ();
}


		public void Remove (string to)
		{
			if(to == null || to.Length == 0) {
				throw new ArgumentNullException ("to");
			}
			_channels.Remove (to);
		}

		public int Count {
			get { return _channels.Values.Count; }
		}

		public SoapChannel this [string index] {
			get { return (SoapChannel) _channels[index]; }
		}

		public ICollection Keys {
			get { return _channels.Keys; }
		}

		public object SyncRoot {
			get { return _channels.SyncRoot; }
		}

		public ICollection Values {
			get { return _channels.Values; }
		}
	}
}

