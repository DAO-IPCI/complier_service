Complier Service package
========================

**Model**: `QmW3dTa1QZxnZzpF9TDuHKN7GDKaJDVoQys4u38xmdAGHF`

The service offsets CO2 footprint by burning VCU tokens

1 MWh of non-renewable electricity produces 1 ton of C02.
1 t of C02 is covered by consumption of 1 VCU.

The payment token is DAI. 1 DAI token is $1

## Scenario

1. A user sends a demand message with the amount of electricity written in objective and the name of the country. The cost is `0`
2. The service calculates the price and sends an offer back
3. If the user agree, a new offer with the price is sent
4. After a liability is created, the service converts the electricity to the amount of VCU tokens and burns it

## Objective topics

* `/geo` - the name of the country
* `/power_kwh` - the amount of the electricity power in kWh

For more information have a look at the [example](robonomics/mybag.bag)

## Build

```
nix build -f release.nix
```

## Launch

By default the agent is set up to work in (sidechain)[https://github.com/airalab/airalab-sidechain] network. To run in a different network change the following properties in the agent.launch file

```
<param name="model" value="QmW3dTa1QZxnZzpF9TDuHKN7GDKaJDVoQys4u38xmdAGHF" />
<param name="token" value="0x7cfd3337F9e423751C9314f9C80cbA57CA2844FE" />
```

To launch manually run:

```
source result/setup.zsh (bash)
roslaunch offsetting_agent agent.launch
```

or as a NixOS service add the following lines to /etc/nixos/configuration.nix:

```
systemd.services.offsetting_agent = {
  enable = true;
  description = "Service for smart building offsetting";
  requires = [ "roscore.service" ];
  after = ["roscore.service" ];
  wantedBy = [ "multi-user.target" ];
  script = ''
    source /var/lib/liability/offsetting_agent/result/setup.bash \
    && roslaunch offsetting_agent agent.launch
  '';
  serviceConfig = {
     Restart = "on-failure";
     StartLimitInterval = 0;
     RestartSec = 60;
     User = "liability";
  };

```

and apply changes:
```
nixos-rebuild switch
```
