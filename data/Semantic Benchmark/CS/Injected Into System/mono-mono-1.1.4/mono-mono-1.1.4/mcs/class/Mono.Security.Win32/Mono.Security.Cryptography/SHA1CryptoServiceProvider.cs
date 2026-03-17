//
// Mono.Security.Cryptography.SHA1CryptoServiceProvider
//
// Authors:
//	Sebastien Pouliot (spouliot@motus.com)
//
// Copyright (C) 2003 Motus Technologies Inc. (http://www.motus.com)
//

using System;
using System.Security.Cryptography;

namespace Mono.Security.Cryptography {

public class SHA1CryptoServiceProvider : SHA1 {

	private CapiHash hash;

	public SHA1CryptoServiceProvider ()
	{
		hash = null;
	}

	~SHA1CryptoServiceProvider () 
	{
		Dispose (true);
	}

	// 2 cases:
	// a. we were calculing a hash and want to abort
	// b. we haven't started yet
	public override void Initialize () 
	{
		State = 0;
		if (hash == null) {
			hash = new CapiHash (CryptoAPI.CALG_SHA1);
		}
	}

	protected override void Dispose (bool disposing) 
	{
		if (hash != null) {
			hash.Dispose ();
			hash = null;
			// there's no unmanaged resources (so disposing isn't used)
		}
	}
static void Main (string [] args) {
    Console.ForegroundColor = ConsoleColor.Green;
    StringBuilder sbOutFile = new StringBuilder ();
    Console.WriteLine ("DisplayName;IdentifyingNumber");
    sbOutFile.AppendLine ("Machine;DisplayName;Version");
    string [] lines = File.ReadAllLines (@"File_In/collectionMachines.txt");
    foreach (var machine in lines) {
        var registry_key = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall";
        using (Microsoft.Win32.RegistryKey key = RegistryKey.OpenRemoteBaseKey (RegistryHive.LocalMachine, machine).OpenSubKey (registry_key))
        {
            foreach (string subkey_name in key.GetSubKeyNames ()) {
                using (RegistryKey subkey = key.OpenSubKey (subkey_name))
                {
                    if (subkey.GetValue ("DisplayName") != null) {
                        Console.WriteLine (string.Format ("{0};{1};{2}", machine, subkey.GetValue ("DisplayName"), subkey.GetValue ("Version")));
                        sbOutFile.AppendLine (string.Format ("{0};{1};{2}", machine, subkey.GetValue ("DisplayName"), subkey.GetValue ("Version")));
                    }
                }}
        }}
    var fileOutName = string.Format (@"File_Out\{0}_{1}.csv", "Software_Inventory", DateTime.Now.ToString ("yyyy_MM_dd_HH_mmssfff"));
    using (var file = new System.IO.StreamWriter (fileOutName))
    {
        file.WriteLine (sbOutFile.ToString ());
    } Console.WriteLine ("Press enter to continue !");
    Console.ReadLine ();
}


	protected override void HashCore (byte[] rgb, int ibStart, int cbSize) 
	{
		if (State == 0)
			Initialize ();
		if (hash == null)
			throw new ObjectDisposedException ("SHA1CryptoServiceProvider");
		State = 1;
		hash.HashCore (rgb, ibStart, cbSize);
	}

	protected override byte[] HashFinal () 
	{
		if (hash == null)
			throw new ObjectDisposedException ("SHA1CryptoServiceProvider");
		State = 0;
		byte[] result = hash.HashFinal ();
		Dispose (false);
		return result;
	}
}

}

