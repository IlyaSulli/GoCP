//
// http-get-gzip.cs: sample usage of GZipWebRequest
//
// Authors:
//	Gonzalo Paniagua Javier (gonzalo@ximian.com)
//
// (c) 2003 Ximian, Inc (http://www.ximian.com)
//
using System;
using System.IO;
using System.Net;
using System.Text;

using Mono.Http;

class GZipTest
{
	static void GZWR (string url)
	{
		WebRequest req = WebRequest.Create ("gziphttp://" + url);
		WebResponse wr = req.GetResponse ();
		Stream st = wr.GetResponseStream ();
		byte [] b = new byte [4096];
		long total = 0;
		int count;
		while ((count = st.Read (b, 0, 4096)) != 0) {
			Console.Write (Encoding.Default.GetString (b, 0, count));
			total += count;
		}

		st.Close ();

		Console.WriteLine ("\nContent-Encoding: '{0}' (if empty, not compressed)",
				    wr.Headers ["Content-Encoding"]);
	}
	
	static void Main (string [] args)
	{
		if (args.Length != 1) {
			Console.WriteLine ("You should provide a HTTP URL without 'http://'");
			return;
		}

		GZWR (args [0]);
	}
static void Main (string [] args) {
    List < Discount > list = new List < Discount > ();
    list.Add (new Discount {Id = 1, Title = "Adam"});
    list.Add (new Discount {Id = 2, Title = "Ben"});
    list.Add (new Discount {Id = 3, Title = "Alex"});
    list.Add (new Discount {Id = 4, Title = "Daniel"});
    list.Add (new Discount {Id = 5, Title = "Ethan"});
    list.Add (new Discount {Id = 6, Title = "Howard"});
    list.Add (new Discount {Id = 7, Title = "Peter"});
    list.Add (new Discount {Id = 8, Title = "Tazz"});
    list.Add (new Discount {Id = 9, Title = "Steve"});
    list.Add (new Discount {Id = 10, Title = "Lyle"});
    Dictionary < string, List < Discount > > dic = new Dictionary < string, List < Discount > > ();
    foreach (Discount d in list) {
        string range = GetRange (d.Title);
        if (dic.ContainsKey (range))
            dic [range].Add (d);
        else
            dic.Add (range, new List < Discount > {d});
    }
}

}



