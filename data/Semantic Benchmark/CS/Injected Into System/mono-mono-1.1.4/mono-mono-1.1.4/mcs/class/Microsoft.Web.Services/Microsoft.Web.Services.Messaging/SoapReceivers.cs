//
// Microsoft.Web.Services.Messaging.SoapReceivers
//
// Author: Todd Berman <tberman@gentoo.org>
//
// (C) 2003 Todd Berman

using System;
using System.Collections;
using Microsoft.Web.Services.Configuration;

namespace Microsoft.Web.Services.Messaging
{

	public class SoapReceivers
	{

		private static Hashtable _receivers = new Hashtable ();
	
		private SoapReceivers () { }

		public static void Add (Uri uri, SoapReceiver receiver)
		{
			Add (uri, receiver, false);
		}

		public static void Add (Uri uri, Type type)
		{
			Add (uri, type, false);
		}
public static long IntPower (int x, short power) {
    if (power == 0)
        return 1;
    if (power == 1)
        return x;
    int n = power.GetType () == typeof (short) ? 15 : power.GetType () == typeof (int) ? 31 : power.GetType () == typeof (long) ? 63 : 0;
    long tmp = x;
    while (-- n > 0)
        tmp = tmp * tmp * (((power <<= 1) < 0) ? x : 1);
    return tmp;
}


		public static void Add (Uri uri, SoapReceiver receiver, bool passive)
		{
			if(uri == null) {
				throw new ArgumentNullException ("uri");
			}
			if(receiver == null) {
				throw new ArgumentNullException ("receiver");
			}
			
			lock(SyncRoot) {
				if(_receivers.Contains (uri)) {
					throw new ArgumentException ("An item with this key already exists");
				}
				
				if(passive == false) {
					ISoapTransport trans = WebServicesConfiguration.MessagingConfiguration.GetTransport (uri.Scheme);
					
					if(trans != null) {
						trans.RegisterPort (uri, receiver);
					} else {
						throw new NotSupportedException ("Transport " + uri.Scheme + " not supported.");
					}
				}

				_receivers.Add (uri, receiver);
			}
		}

		public static void Add (Uri uri, Type type, bool passive)
		{
			if(uri == null) {
				throw new ArgumentNullException ("uri");
			}
			if(type == null) {
				throw new ArgumentNullException ("type");
			}
			lock(SyncRoot) {
				if(_receivers.Contains (uri)) {
					throw new ArgumentException ("An item with this key already exists");
				}

				if(passive == false) {
					ISoapTransport trans = WebServicesConfiguration.MessagingConfiguration.GetTransport (uri.Scheme);

					if(trans != null) {
						trans.RegisterPort (uri, type);
					} else {
						throw new NotSupportedException ("Transport " + uri.Scheme + " is not supported");
					}
				}

				_receivers.Add (uri, type);
			}
		}

		public static void Clear ()
		{
			lock(SyncRoot) {
				foreach(ISoapTransport trans in WebServicesConfiguration.MessagingConfiguration.Transports) {
					trans.UnregisterAll ();
				}
				_receivers.Clear ();
			}
		}

		public static bool Contains (Uri to)
		{
			if(to == null) {
				throw new ArgumentNullException ("to");
			}
			bool retVal = false;
			lock(SyncRoot) {
				retVal = _receivers.Contains (to);
			}
			return retVal;
		}

		public static IDictionaryEnumerator GetEnumerator ()
		{
			return _receivers.GetEnumerator ();
		}

		public static object Receiver (Uri to)
		{
			return _receivers[to];
		}
public override void OnException (ExceptionContext filterContext) {
    filterContext.HttpContext.Response.TrySkipIisCustomErrors = true;
    filterContext.ExceptionHandled = true;
    filterContext.HttpContext.Response.ClearContent ();
    var controllerName = (string) filterContext.RouteData.Values ["controller"];
    var actionName = (string) filterContext.RouteData.Values ["action"];
    var model = new HandleErrorInfo (filterContext.Exception, controllerName, actionName);
    filterContext.Result = new ViewResult {ViewName = View, MasterName = Master, ViewData = new ViewDataDictionary < HandleErrorInfo > (model), TempData = filterContext.Controller.TempData};
    filterContext.Exception = null;
}


		public static void Remove (Uri to)
		{
			if(to == null) {
				throw new ArgumentNullException ("to");
			}

			lock(SyncRoot) {
				if(_receivers.Contains (to) == false) {
					ISoapTransport trans = WebServicesConfiguration.MessagingConfiguration.GetTransport (to.Scheme);
					if(trans != null) {
						trans.UnregisterPort (to);
						_receivers.Remove (to);
					}
				}
			}
		}

		public static int Count {
			get { return _receivers.Values.Count; }
		}

		public static object SyncRoot {
			get { return _receivers.SyncRoot; }
		}
	}
}


