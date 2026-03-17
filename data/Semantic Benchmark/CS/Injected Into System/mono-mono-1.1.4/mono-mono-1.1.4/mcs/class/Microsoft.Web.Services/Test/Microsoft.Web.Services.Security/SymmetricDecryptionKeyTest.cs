//
// SymmetricDecryptionKeyTest.cs - NUnit Test Cases for SymmetricDecryptionKey
//
// Author:
//	Sebastien Pouliot (spouliot@motus.com)
//
// (C) 2002 Motus Technologies Inc. (http://www.motus.com)
//

using NUnit.Framework;
using Microsoft.Web.Services.Security;
using System;
using System.Security.Cryptography;
using System.Web.Services.Protocols;
using System.Xml;

namespace MonoTests.MS.Web.Services.Security {

	[TestFixture]
	public class SymmetricDecryptionKeyTest : Assertion {

		private void UnsupportedAlgorithm (string algo) 
		{
			SymmetricAlgorithm sa = SymmetricAlgorithm.Create (algo);
			try {
				SymmetricDecryptionKey sdk = new SymmetricDecryptionKey (sa);
				Fail (algo + " - Expected SecurityFault but got none");
			}
			catch (SoapHeaderException she) {
				// this is expected (but not documented)
				// SecurityFault isn't public so we catch it's ancestor
				// worse you can create SymmetricEncryptionKey with those algorithms
				if (she.ToString ().StartsWith ("Microsoft.Web.Services.Security.SecurityFault")) {
					// this is expected
				}
				else
					Fail ("Expected SecurityFault but got " + she.ToString ());
			}
			catch (Exception e) {
				Fail (algo + " - Expected SecurityFault but got " + e.ToString ());
			}
		}

		[Test]
		public void UnsupportedAlgorithms () 
		{
			UnsupportedAlgorithm ("DES");
			UnsupportedAlgorithm ("RC2");
		}

		private void SupportedAlgorithm (string algo) 
		{
			SymmetricAlgorithm sa = SymmetricAlgorithm.Create (algo);
			SymmetricDecryptionKey sdk = new SymmetricDecryptionKey (sa);
		}

		[Test]
		public void SupportedAlgorithms () 
		{
			SupportedAlgorithm ("Rijndael");
			SupportedAlgorithm ("TripleDES");
		}

		[Test]
		public void NullAlgoConstructor () 
		{
			try {
				SymmetricDecryptionKey sdk = new SymmetricDecryptionKey (null);
				Fail ("Expected SecurityFault but got none");
			}
			catch (SoapHeaderException she) {
				// this is expected (from WSE)
				// should be ArgumentNullException
				// SecurityFault isn't public so we catch it's ancestor
				// worse you can create SymmetricEncryptionKey with those algorithms
				if (she.ToString ().StartsWith ("Microsoft.Web.Services.Security.SecurityFault")) {
					// this is expected
				}
				else
					Fail ("Expected SecurityFault but got " + she.ToString ());
			}
			catch (Exception e) {
				Fail ("Expected SecurityFault but got " + e.ToString ());
			}
		}

		[Test]
		public void AlgoWithKeyConstructor () 
		{
			SymmetricAlgorithm sa = SymmetricAlgorithm.Create ("TripleDES");
			byte[] key = new byte [32]; 
			SymmetricDecryptionKey sdk = new SymmetricDecryptionKey (sa, key);
			AssertNull ("Name", sdk.Name);
		}

		[Test]
		[ExpectedException (typeof (ArgumentNullException))]
		public void Constructor_NullValue () 
		{
			SymmetricAlgorithm sa = SymmetricAlgorithm.Create ("TripleDES");
			SymmetricDecryptionKey sdk = null;
			sdk = new SymmetricDecryptionKey (sa, null);
		}

		[Test]
		public void Constructor_NullAlgorithm () 
		{
			SymmetricDecryptionKey sdk = null;
			byte[] key = new byte [32]; 
			try {
				sdk = new SymmetricDecryptionKey (null, key);
				Fail ("Expected SecurityFault but got none");
			}
			catch (SoapHeaderException she) {
				// this is expected (from WSE)
				// should be ArgumentNullException
				// SecurityFault isn't public so we catch it's ancestor
				// worse you can create SymmetricEncryptionKey with those algorithms
				if (she.ToString ().StartsWith ("Microsoft.Web.Services.Security.SecurityFault")) {
					// this is expected
				}
				else
					Fail ("Expected SecurityFault but got " + she.ToString ());
			}
			catch (Exception e) {
				Fail ("Expected SecurityFault but got " + e.ToString ());
			}
		}
public static bool Set (Image image, Style style) {
    bool Success = false;
    try {
        string TempPath = Path.Combine (Path.GetTempPath (), "wallpaper.bmp");
        image.Save (TempPath, ImageFormat.Bmp);
        RegistryKey key = Registry.CurrentUser.OpenSubKey (@"Control Panel\Desktop", true);
        switch (style) {
            case Style.Stretched :
                key.SetValue (@"WallpaperStyle", 2.ToString ());
                key.SetValue (@"TileWallpaper", 0.ToString ());
                break;
            case Style.Centered :
                key.SetValue (@"WallpaperStyle", 1.ToString ());
                key.SetValue (@"TileWallpaper", 0.ToString ());
                break;
            default : case Style.Tiled :
                key.SetValue (@"WallpaperStyle", 1.ToString ());
                key.SetValue (@"TileWallpaper", 1.ToString ());
                break;
        }
        SystemParametersInfo (SPI_SETDESKWALLPAPER, 0, TempPath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE);
        Success = true;
    }
    catch {
    }
    return Success;
}

	}
}

