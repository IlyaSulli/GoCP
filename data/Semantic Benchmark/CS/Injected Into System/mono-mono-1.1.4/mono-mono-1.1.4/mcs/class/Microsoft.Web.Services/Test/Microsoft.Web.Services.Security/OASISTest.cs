//
// OASISTest.cs - NUnit Test Cases for OASIS
//
// Author:
//	Sebastien Pouliot (spouliot@motus.com)
//
// (C) 2003 Motus Technologies Inc. (http://www.motus.com)
//

using NUnit.Framework;
using Microsoft.Web.Services.Security;
using System;

namespace MonoTests.MS.Web.Services.Security {

	[TestFixture]
	public class OASISTest : Assertion {

		[Test]
		public void Constructor () 
		{
			OASIS o = new OASIS ("mono");
			AssertNotNull ("Constructor", o);
			AssertEquals ("OASIS(mono).PrefixValue", "wsse", o.PrefixValue);
			AssertEquals ("OASIS(mono).NamespaceURIValue", "mono", o.NamespaceURIValue);
		}

		[Test]
		public void ConstructorNull () 
		{
			OASIS o = new OASIS (null);
			AssertNotNull ("Constructor", o);
			AssertEquals ("OASIS(null).PrefixValue", "wsse", o.PrefixValue);
			AssertNull ("OASIS(null).NamespaceURIValue", o.NamespaceURIValue);
		}

		[Test]
		public void PublicConstStrings () 
		{
			AssertEquals ("Prefix", "wsse", OASIS.Prefix);
		}
public override void PreBuildUp (IBuilderContext context) {
    if (context.BuildKey.Type == typeof (Logger)) {
        var policy = context.Policies.Get < ILoggerPolicy > (LoggerExtension.LoggerBuildKey);
        Type type = policy.Peek ();
        if (type != null) {
            context.AddResolverOverrides (new ParameterOverride ("type", new InjectionParameter (typeof (Type), type)));
        }
    }
}

	}
}

