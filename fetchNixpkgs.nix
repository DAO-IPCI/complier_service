{ rev    ? "b8abf91a11ad0e5f8492f3c6ec66f18d57c26e92"             # The Git revision of nixpkgs to fetch
, sha256 ? "08wpjki78rbn4ncv550xxsb1pxlsgln9nr8qw4ilb7lkicy8jk1d" # The SHA256 of the downloaded data
}:

builtins.fetchTarball {
  url = "https://github.com/airalab/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}
