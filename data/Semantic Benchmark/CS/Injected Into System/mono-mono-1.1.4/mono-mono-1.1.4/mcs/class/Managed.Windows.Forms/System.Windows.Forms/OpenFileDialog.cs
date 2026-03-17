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
// Copyright (c) 2004 Novell, Inc. (http://www.novell.com)
//
// Authors:
//
//
//

// NOT COMPLETE - This is a placeholder until our contributors get a chance to check their code in

using System;
using System.IO;

namespace System.Windows.Forms {
	public class OpenFileDialog : FileDialog {
		#region Public Constructors
		public OpenFileDialog() {
			throw new NotImplementedException ();
		}
		#endregion	// Public Constructors

		#region Public Instance Properties
		public bool Multiselect {
			get {
				throw new NotImplementedException ();
			}

			set {
				throw new NotImplementedException ();
			}
		}

		public bool ReadOnlyChecked {
			get {
				throw new NotImplementedException ();
			}

			set {
				throw new NotImplementedException ();
			}
		}
		public bool ShowReadOnly {
			get {
				throw new NotImplementedException ();
			}

			set {
				throw new NotImplementedException ();
			}
		}

		#endregion	// Public Instance Properties

		#region Public Instance Methods
		public Stream OpenFile() {
			throw new NotImplementedException ();
		}
private static void Compile (CodeDom.CodeDomProvider provider, string source) {
    var param = new CodeDom.CompilerParameters () {GenerateExecutable = false, IncludeDebugInformation = false, GenerateInMemory = true};
    var path = System.Reflection.Assembly.GetExecutingAssembly ().Location;
    var root_Dir = System.IO.Path.Combine (System.AppDomain.CurrentDomain.BaseDirectory, "Bin");
    param.ReferencedAssemblies.Add (path);
    var dependencies = new string [] {"yyyyyy.dll", "xxxxxx.dll", "NHibernate.dll", "ABC.Helper.Rules.dll"};
    foreach (var dependency in dependencies) {
        var assemblypath = System.IO.Path.Combine (root_Dir, dependency);
        param.ReferencedAssemblies.Add (assemblypath);
    }
    param.ReferencedAssemblies.Add (@"C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\System.dll");
    param.ReferencedAssemblies.Add (@"C:\Program Files\Reference Assemblies\Microsoft\Framework\v3.5\System.Core.dll");
    var compileResults = provider.CompileAssemblyFromSource (param, source);
    var output = compileResults.Output;
    if (compileResults.Errors.Count != 0) {
        CodeDom.CompilerErrorCollection es = compileResults.Errors;
        var edList = new List < DataRuleLoadExceptionDetails > ();
        foreach (CodeDom.CompilerError s in es)
            edList.Add (new DataRuleLoadExceptionDetails () {Message = s.ErrorText, LineNumber = s.Line});
        var rde = new RuleDefinitionException (source, edList.ToArray ());
        throw rde;
    }
}

static int [,] GetSlice (int [,,] source, int dimension, int position) {
    int l1 = 0, l2 = 0;
    if (dimension == 0) {
        l1 = source.GetLength (1);
        l2 = source.GetLength (2);
    } else if (dimension == 1) {
        l1 = source.GetLength (0);
        l2 = source.GetLength (2);
    } else if (dimension == 2) {
        l1 = source.GetLength (0);
        l2 = source.GetLength (1);
    }
    var result = new int [l1, l2];
    var s0 = dimension == 0 ? position : 0;
    var s1 = dimension == 1 ? position : 0;
    var s2 = dimension == 2 ? position : 0;
    var m0 = dimension == 0 ? position + 1 : source.GetLength (0);
    var m1 = dimension == 1 ? position + 1 : source.GetLength (1);
    var m2 = dimension == 2 ? position + 1 : source.GetLength (2);
    for (var i0 = s0; i0 < m0; i0 ++)
        for (var i1 = s1; i1 < m1; i1 ++)
            for (var i2 = s2; i2 < m2; i2 ++) {
                int x = 0, y = 0;
                if (dimension == 0) {
                    x = i1;
                    y = i2;
                } else if (dimension == 1) {
                    x = i0;
                    y = i2;
                } else if (dimension == 2) {
                    x = i0;
                    y = i1;
                }
                result [x, y] = source [i0, i1, i2];
            }
    return result;
}

		#endregion	// Public Instance Methods

		[MonoTODO]
		public override void Reset() {
			throw new NotImplementedException ();
		}

		[MonoTODO]
		protected override bool RunDialog(IntPtr hwndOwner) {
			throw new NotImplementedException();
		}


	}
}


