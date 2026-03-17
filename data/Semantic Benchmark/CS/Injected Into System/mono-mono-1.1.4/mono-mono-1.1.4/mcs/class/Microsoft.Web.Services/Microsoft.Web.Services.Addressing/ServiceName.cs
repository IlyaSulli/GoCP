//
// Microsoft.Web.Services.Addressing.ServiceName.cs
//
// Author: Todd Berman <tberman@gentoo.org>
//
// (C) 2003 Todd Berman

using System;
using System.Xml;
using Microsoft.Web.Services.Xml;

namespace Microsoft.Web.Services.Addressing
{
	public class ServiceName : AttributedQName, IXmlElement
	{
		private string _port;

		public ServiceName (XmlElement element) : base ()
		{
			LoadXml (element);
		}

		public ServiceName (QualifiedName qname) : base (qname)
		{
		}

		[MonoTODO]
		public XmlElement GetXml (XmlDocument document)
		{
			throw new NotImplementedException ();
		}
private void SetTableDescriptions (Type tableType) {
    string fullTableName = context.GetTableName (tableType);
    Regex regex = new Regex (@"(\[\w+\]\.)?\[(?<table>.*)\]");
    Match match = regex.Match (fullTableName);
    string tableName;
    if (match.Success)
        tableName = match.Groups ["table"].Value;
    else
        tableName = fullTableName;
    var tableAttrs = tableType.GetCustomAttributes (typeof (TableAttribute), false);
    if (tableAttrs.Length > 0)
        tableName = ((TableAttribute) tableAttrs [0]).Name;
    foreach (var prop in tableType.GetProperties (System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.Instance)) {
        if (prop.PropertyType.IsClass && prop.PropertyType != typeof (string))
            continue;
        var attrs = prop.GetCustomAttributes (typeof (DisplayAttribute), false);
        if (attrs.Length > 0)
            SetColumnDescription (tableName, prop.Name, ((DisplayAttribute) attrs [0]).Name);
    }
}


		[MonoTODO]
		public void LoadXml (XmlElement element)
		{
			throw new NotImplementedException ();
		}

		public string PortName {
			get { return _port; }
			set { _port = value; }
		}
	}
}

