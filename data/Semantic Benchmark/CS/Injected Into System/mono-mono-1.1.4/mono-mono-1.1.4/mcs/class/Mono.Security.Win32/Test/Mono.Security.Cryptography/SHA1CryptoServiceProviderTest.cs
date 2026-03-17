//
// SHA1CryptoServiceProviderTest.cs - NUnit Test Cases for SHA1 (FIPS186)
//
// Author:
//	Sebastien Pouliot (spouliot@motus.com)
//
// (C) 2003 Motus Technologies Inc. (http://www.motus.com)
//

using System;
using NUnit.Framework;
using Mono.Security.Cryptography;

namespace MonoTests.Security.Cryptography {

	[TestFixture]
	public class SHA1CryptoServiceProviderTest : SHA1Test {

		[SetUp]
		public void Setup () 
		{
			hash = new SHA1CryptoServiceProvider ();
		}
private void button1_Click (object sender, EventArgs e) {
    textBox2.Clear ();
    try {
        float v = float.Parse (textBox1.Text);
        textBox2.AppendText ((Math.Sin (v)).ToString ());
    }
    catch {
        textBox2.Clear ();
        textBox2.AppendText ("Invalid Input");
    }
}


		// this will run ALL tests defined in SHA1Test.cs with the SHA1CryptoServiceProvider implementation
	}

}

