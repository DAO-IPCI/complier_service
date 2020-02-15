{ rev    ? "82e69652b8c59810bc9214ddbfe9daafccd37b15"             # The Git revision of nixpkgs to fetch
, sha256 ? "16bhwi8x964hqh11dp9qw1ja1s098fdyb2v25y9bb9qfg2riyc9l" # The SHA256 of the downloaded data
}:

builtins.fetchTarball {
  url = "https://github.com/airalab/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}
