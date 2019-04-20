{ stdenv
, mkRosPackage
, robonomics_comm 
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "complier_service";
  version = "master";

  src = ./.;

  propagatedBuildInputs = [ robonomics_comm ];

  meta = with stdenv.lib; {
    description = "Simple modular AIRA example effort";
    homepage = http://github.com/airalab/complier_service;
    license = licenses.bsd3;
    maintainers = with maintainers; [ akru ];
  };
}
