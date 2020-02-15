{ stdenv
, mkRosPackage
, robonomics_comm-nightly
, python3Packages
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "offsetting_agent";
  version = "0.2.1";

  src = ./.;

  propagatedBuildInputs = with python3Packages; [
    robonomics_comm-nightly
    python3Packages.pinatapy
  ];

  meta = with stdenv.lib; {
    description = "Carbon neutrality as a service";
    homepage = http://github.com/dao-ipci/offsetting_agent;
    license = licenses.bsd3;
    maintainers = with maintainers; [ vourhey ];
  };
}
