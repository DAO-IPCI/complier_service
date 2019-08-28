{ stdenv
, mkRosPackage
, robonomics_comm-nightly
, python3Packages
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "complier_service";
  version = "master";

  src = ./.;

  propagatedBuildInputs = with python3Packages; [ robonomics_comm-nightly ];

  meta = with stdenv.lib; {
    description = "Carbon neutrality as a service";
    homepage = http://github.com/dao-ipce/complier_service;
    license = licenses.bsd3;
    maintainers = with maintainers; [ vourhey ];
  };
}
