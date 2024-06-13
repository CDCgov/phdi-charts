# Charts

The charts in the `charts/` directory are based on services maintained by DIBBs in the [phdi repository](https://github.com/CDCgov/phdi). These helm charts ensure that Terraform can build each of these services to be able to deployed online for any individual to access without needing to install and run a given service locally.

## Version

The latest version of these charts can be determined by reviewing the latest Release, which can be found [here](https://github.com/CDCgov/phdi/releases).

For the purposes of best practices with helm charts, we do not update the version numbers in a given chart's `values.yaml` but rather dynamically update them with the latest Release version at the time of deployment to the cloud.

If you wish to deploy the charts outside of that cloud deployment, we recommend checking and updating the `values.yaml` for the respective chart or running [helm upgrade](https://helm.sh/docs/helm/helm_upgrade/).
