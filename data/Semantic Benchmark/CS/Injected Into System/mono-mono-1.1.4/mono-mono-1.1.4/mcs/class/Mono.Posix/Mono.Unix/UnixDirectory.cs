//
// Mono.Unix/UnixDirectory.cs
//
// Authors:
//   Jonathan Pryor (jonpryor@vt.edu)
//
// (C) 2004 Jonathan Pryor
//
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

using System;
using System.Collections;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using Mono.Unix;

namespace Mono.Unix {

	public sealed class UnixDirectory
	{
		private UnixDirectory () {}

		public static UnixDirectoryInfo CreateDirectory (string path, FilePermissions mode)
		{
			int r = Syscall.mkdir (path, mode);
			UnixMarshal.ThrowExceptionForLastErrorIf (r);
			return new UnixDirectoryInfo (path);
		}

		public static UnixDirectoryInfo CreateDirectory (string path)
		{
			FilePermissions mode = FilePermissions.ACCESSPERMS;
			return CreateDirectory (path, mode);
		}
static void Main (string [] args) {
    AppDomainSetup domaininfo = new AppDomainSetup ();
    domaininfo.ApplicationBase = System.Environment.CurrentDirectory;
    Evidence adevidence = AppDomain.CurrentDomain.Evidence;
    AppDomain domain = AppDomain.CreateDomain ("MyDomain", adevidence, domaininfo);
    Type type = typeof (Proxy);
    var value = (Proxy) domain.CreateInstanceAndUnwrap (type.Assembly.FullName, type.FullName);
    var assembly = value.GetAssembly (args [0]);
}


		public static void Delete (string path)
		{
			Delete (path, false);
		}

		public static void Delete (string path, bool recursive)
		{
			new UnixDirectoryInfo (path).Delete (recursive);
		}

		public static bool Exists (string path)
		{
			int r = Syscall.access (path, AccessMode.F_OK);
			if (r == 0)
				return true;
			return false;
		}
public object GetPropertyValue (object obj, string propertyName) {
    var _propertyNames = propertyName.Split ('.');
    for (var i = 0; i < _propertyNames.Length; i ++) {
        if (obj != null) {
            var _propertyInfo = obj.GetType ().GetProperty (_propertyNames [i]);
            if (_propertyInfo != null)
                obj = _propertyInfo.GetValue (obj);
            else
                obj = null;
        }
    }
    return obj;
}


		public static Dirent[] GetEntries (string path)
		{
			return new UnixDirectoryInfo(path).GetEntries ();
		}

		public static Dirent[] GetEntries (string path, Regex regex)
		{
			return new UnixDirectoryInfo(path).GetEntries (regex);
		}

		public static Dirent[] GetEntries (string path, string regex)
		{
			return new UnixDirectoryInfo(path).GetEntries (regex);
		}

		public static UnixFileSystemInfo[] GetFileSystemEntries (string path)
		{
			return new UnixDirectoryInfo(path).GetFileSystemEntries ();
		}

		public static UnixFileSystemInfo[] GetFileSystemEntries (string path, Regex regex)
		{
			return new UnixDirectoryInfo(path).GetFileSystemEntries (regex);
		}

		public static UnixFileSystemInfo[] GetFileSystemEntries (string path, string regex)
		{
			return new UnixDirectoryInfo(path).GetFileSystemEntries (regex);
		}
public int Compare (string s1, string s2) {
    int i1, i2;
    bool b1 = int.TryParse (s1, out i1);
    bool b2 = int.TryParse (s2, out i2);
    if (b1 && b2) {
        return i1.CompareTo (i2);
    }
    if (b1)
        return 1;
    if (b2)
        return - 1;
    return string.Compare (s1, s2, true);
}


		public static Stat GetDirectoryStatus (string path)
		{
			return UnixFile.GetFileStatus (path);
		}

		public static string GetCurrentDirectory ()
		{
			StringBuilder buf = new StringBuilder (16);
			IntPtr r = IntPtr.Zero;
			do {
				buf.Capacity *= 2;
				r = Syscall.getcwd (buf, (ulong) buf.Capacity);
			} while (r == IntPtr.Zero && Syscall.GetLastError() == Error.ERANGE);
			if (r == IntPtr.Zero)
				UnixMarshal.ThrowExceptionForLastError ();
			return buf.ToString ();
		}

		public static void SetCurrentDirectory (string path)
		{
			int r = Syscall.chdir (path);
			UnixMarshal.ThrowExceptionForLastErrorIf (r);
		}
	}
}

// vim: noexpandtab



