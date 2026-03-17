//
// For System.Security.Cryptography.Xml
//	Signature.cs - Signature implementation for XML Signature
// For Microsoft.Web.Services.Security
//	SignedXmlSignature.cs
//
// Author:
//	Sebastien Pouliot (spouliot@motus.com)
//
// (C) 2002, 2003 Motus Technologies Inc. (http://www.motus.com)
//

using System;
using System.Collections;
using System.Security.Cryptography;
using System.Xml;

#if (WSE1 || WSE2)
using System.Security.Cryptography.Xml;

namespace Microsoft.Web.Services.Security {

	public class SignedXmlSignature {

		public SignedXmlSignature () 
#else
namespace System.Security.Cryptography.Xml {

	public class Signature {

		public Signature () 
#endif
		{
			list = new ArrayList ();
		}

		private ArrayList list;
		private SignedInfo info;
		private KeyInfo key;
		private string id;
		private byte[] signature;

		public string Id {
			get { return id; }
			set { id = value; }
		}

		public KeyInfo KeyInfo {
			get { return key; }
			set { key = value; }
		}

		public IList ObjectList {
			get { return list; }
			set { list = ArrayList.Adapter (value); }
		}

		public byte[] SignatureValue {
			get { return signature; }
			set { signature = value; }
		}

		public SignedInfo SignedInfo {
			get { return info; }
			set { info = value; }
		}

		public void AddObject (DataObject dataObject) 
		{
			list.Add (dataObject);
		}

		public XmlElement GetXml () 
		{
			if (info == null)
				throw new CryptographicException ("SignedInfo");
			if (signature == null)
				throw new CryptographicException ("SignatureValue");

			XmlDocument document = new XmlDocument ();
			XmlElement xel = document.CreateElement (XmlSignature.ElementNames.Signature, XmlSignature.NamespaceURI);
			if (id != null)
				xel.SetAttribute (XmlSignature.AttributeNames.Id, id);

			XmlNode xn = info.GetXml ();
			XmlNode newNode = document.ImportNode (xn, true);
			xel.AppendChild (newNode);

			if (signature != null) {
				XmlElement sv = document.CreateElement (XmlSignature.ElementNames.SignatureValue, XmlSignature.NamespaceURI);
				sv.InnerText = Convert.ToBase64String (signature);
				xel.AppendChild (sv);
			}

			if (key != null) {
				xn = key.GetXml ();
				newNode = document.ImportNode (xn, true);
				xel.AppendChild (newNode);
			}

			if (list.Count > 0) {
				foreach (DataObject obj in list) {
					xn = obj.GetXml ();
					newNode = document.ImportNode (xn, true);
					xel.AppendChild (newNode);
				}
			}

			return xel;
		}
private void OnUnhandledApplicationException (object sender, EventArgs e) {
    StringBuilder message = new StringBuilder ("<html><head><style>" + "body, table { font-size: 12px; font-family: Arial, sans-serif; }\r\n" + "table tr td { padding: 4px; }\r\n" + ".header { font-weight: 900; font-size: 14px; color: #fff; background-color: #2b4e74; }\r\n" + ".header2 { font-weight: 900; background-color: #c0c0c0; }\r\n" + "</style></head><body><table><tr><td class=\"header\"><![CDATA[\r\n\r\nUnhandled Exception logged by LogModule.dll:\r\n\r\nappId=");
    string appId = (string) AppDomain.CurrentDomain.GetData (".appId");
    if (appId != null) {
        message.Append (appId);
    }
    message.Append ("</td></tr>");
    HttpServerUtility server = HttpContext.Current.Server;
    Exception currentException = server.GetLastError ();
    if (currentException != null) {
        message.AppendFormat ("<tr><td class=\"header2\"><![CDATA[TYPE</td></tr><tr><td>{0}</td></tr><tr><td class=\"header2\"><![CDATA[REQUEST</td></tr><tr><td>{3}</td></tr><tr><td class=\"header2\"><![CDATA[MESSAGE</td></tr><tr><td>{1}</td></tr><tr><td class=\"header2\"><![CDATA[STACK TRACE</td></tr><tr><td>{2}</td></tr>", currentException.GetType ().FullName, currentException.Message, currentException.StackTrace, HttpContext.Current != null ? HttpContext.Current.Request.FilePath : "n/a");
        server.ClearError ();
    }
    message.Append ("</table></body></html>");
    HttpContext.Current.Response.Write (message.ToString ());
    server.ClearError ();
}

public static void Main () {
    List < bool > mouseStates = new List < bool > {false, false, false, false, true, true, true, false, true, false, false, true};
    mouseStates.Zip (mouseStates.Skip (1), (oldMouseState, newMouseState) = > {
        if (oldMouseState) {
            if (newMouseState)
                return MouseEvent.Held;
            else
                return MouseEvent.Released;
        } else {
            if (newMouseState)
                return MouseEvent.Clicked;
            else
                return MouseEvent.NotPressed;
        }
    }).ToList ().ForEach (mouseEvent = > Console.WriteLine (mouseEvent));
}


		private string GetAttribute (XmlElement xel, string attribute) 
		{
			XmlAttribute xa = xel.Attributes [attribute];
			return ((xa != null) ? xa.InnerText : null);
		}

		public void LoadXml (XmlElement value) 
		{
			if (value == null)
				throw new ArgumentNullException ("value");

			if ((value.LocalName == XmlSignature.ElementNames.Signature) && (value.NamespaceURI == XmlSignature.NamespaceURI)) {
				id = GetAttribute (value, XmlSignature.AttributeNames.Id);

				XmlNodeList xnl = value.GetElementsByTagName (XmlSignature.ElementNames.SignedInfo);
				if ((xnl != null) && (xnl.Count == 1)) {
					info = new SignedInfo ();
					info.LoadXml ((XmlElement) xnl[0]);
				}

				xnl = value.GetElementsByTagName (XmlSignature.ElementNames.SignatureValue);
				if ((xnl != null) && (xnl.Count == 1)) {
					signature = Convert.FromBase64String (xnl[0].InnerText);
				}

				xnl = value.GetElementsByTagName (XmlSignature.ElementNames.KeyInfo);
				if ((xnl != null) && (xnl.Count == 1)) {
					key = new KeyInfo ();
					key.LoadXml ((XmlElement) xnl[0]);
				}

				xnl = value.GetElementsByTagName (XmlSignature.ElementNames.Object);
				if ((xnl != null) && (xnl.Count > 0)) {
					foreach (XmlNode xn in xnl) {
						DataObject obj = new DataObject ();
						obj.LoadXml ((XmlElement) xn);
						AddObject (obj);
					}
				}
			}

			// if invalid
			if (info == null)
				throw new CryptographicException ("SignedInfo");
			if (signature == null)
				throw new CryptographicException ("SignatureValue");
		}
	}
}


