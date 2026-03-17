using System;
using NUnit.Framework;
using System.Xml;
using Microsoft.Web.Services;

namespace Microsoft.Web.Services.Addressing.Tests
{
	
	[TestFixture]
	public class ActionTest
	{
		
		[Test]
		public void CreateAction ()
		{
			Action a = new Action("urn:action:test");
			Assert.IsTrue (a.Value == "urn:action:test");
		}
		
		[Test]
		public void ActionToXml ()
		{
			Action a = new Action("urn:action:test");
			XmlElement element = a.GetXml(new XmlDocument());
			Assert.IsTrue (element.OuterXml.Length != 0);
		}
		
		[Test]
		public void XmlToAction ()
		{
			XmlDocument document = new XmlDocument ();
			
			XmlElement element = document.CreateElement("wsa", "Action", "http://schemas.xmlsoap.org/ws/2003/03/addressing");
			element.InnerText = "urn:action:test";
			
			Action a = new Action (element);
			
			Assert.IsTrue (a.Value == "urn:action:test");
		}
		
		[Test]
		public void RoundTripFromAction ()
		{
			Action a = new Action ("urn:action:test");
			XmlElement element = a.GetXml(new XmlDocument());
			
			Action b = new Action (element);
			
			Assert.IsTrue (b.Value == "urn:action:test");
		}
		
		[Test]
		public void RoundTripFromXml ()
		{
			XmlDocument document = new XmlDocument ();
			
			XmlElement element = document.CreateElement("wsa", "Action", "http://schemas.xmlsoap.org/ws/2003/03/addressing");
			element.InnerText = "urn:action:test";
			
			Action a = new Action (element);
			
			XmlElement element2 = a.GetXml(new XmlDocument ());
			
			Assert.IsTrue (element.OuterXml == element2.OuterXml);
			
		}
		
		[Test]
		public void ImplicitString ()
		{
			Action a = new Action ("urn:action:test");
			
			Assert.IsTrue ("urn:action:test" == a);
		}
static void Main (string [] args) {
    double d = double.NaN;
    for (int test = 0; test < 10; ++ test) {
        var sw1 = Stopwatch.StartNew ();
        bool result1 = false;
        for (int ix = 0; ix < 1000 * 1000; ++ ix) {
            result1 |= double.IsNaN (d);
        }
        sw1.Stop ();
        var sw2 = Stopwatch.StartNew ();
        bool result2 = false;
        for (int ix = 0; ix < 1000 * 1000; ++ ix) {
            result2 |= IsNaN (d);
        }
        sw2.Stop ();
        Console.WriteLine ("{0} - {1} x {2}%", sw1.Elapsed, sw2.Elapsed, 100 * sw2.ElapsedTicks / sw1.ElapsedTicks, result1, result2);
    }
    Console.ReadLine ();
}

		
		[Test]
		public void ImplicitAction ()
		{
			Action a = "urn:action:test";
			
			Assert.IsTrue ("urn:action:test" == a);
			
		}
		
		[Test]
		[ExpectedException(typeof(ArgumentException))]
		public void InvalidElementExceptionTest ()
		{
			XmlDocument doc = new XmlDocument ();
			
			XmlElement el = doc.CreateElement("b", "a", "d");
			
			Action a = new Action (el);
		}
		
	}
	
	
}

