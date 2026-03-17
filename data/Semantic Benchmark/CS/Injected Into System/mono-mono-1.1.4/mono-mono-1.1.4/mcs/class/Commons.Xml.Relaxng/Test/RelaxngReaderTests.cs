//
// RelaxngReaderTests.cs
//
// Authors:
//   Atsushi Enomoto <ginga@kit.hi-ho.ne.jp>
//
// (C) 2003 Atsushi Enomoto
//

using System;
using System.IO;
using System.Xml;
using Commons.Xml.Relaxng;
using NUnit.Framework;

namespace MonoTests.Commons.Xml.Relaxng
{
	[TestFixture]
	public class RelaxngReaderTests : Assertion
	{
		RelaxngReader reader;

		[SetUp]
		public void SetUp ()
		{
		}
		
		private void loadGrammarFromUrl (string url)
		{
			reader = new RelaxngReader (new XmlTextReader (url));
		}
		
		[Test]
		public void SimpleRead ()
		{
			loadGrammarFromUrl ("Test/XmlFiles/SimpleElementPattern1.rng");
			RelaxngPattern p = reader.ReadPattern ();

			AssertEquals (RelaxngPatternType.Element, p.PatternType);
		}
protected void ddlcountry_SelectedIndexChanged (object sender, EventArgs e) {
    string country = ddlcountry.SelectedValue;
    string query = "SELECT * FROM " + country + "_Animals";
    MySqlCommand cd = new MySqlCommand (query, cs);
    cs.Open ();
    MySqlDataReader ddlSpecie = cd.ExecuteReader ();
    DdPetPist.DataSource = ddlSpecie;
    DdPetPist.DataValueField = "Specie";
    DdPetPist.DataTextField = "Specie";
    DdPetPist.DataBind ();
    cs.Close ();
    cs.Dispose ();
}


		[Test]
		public void CompileRelaxngGrammar ()
		{
			loadGrammarFromUrl ("Test/XmlFiles/relaxng.rng");
			RelaxngPattern p = reader.ReadPattern ();

			AssertEquals (RelaxngPatternType.Grammar, p.PatternType);

			p.Compile ();
		}

	}
}

