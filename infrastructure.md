# Computing infrastructure
The CYGNO exepriment develop a facility based on the [INFN cloud](https://www.cloud.infn.it/) to host:
- services for experiment monitoring, data analysis and simulation [status and access page](https://notebook.cygno.cloud.infn.it) 
- data experiment storage ([S3 based](https://it.wikipedia.org/wiki/Amazon_S3)) - [status](https://t1metria.cr.cnaf.infn.it/d/000000123/bucket-s3-cygno?orgId=18)
- tape backup storage - [status](https://t1metria.cr.cnaf.infn.it/d/ZArHZvEMz/storage-usage-per-experiment?orgId=18&var-exp=cygn&var-vo=CYGNO&from=now-30d&to=now) 
- bach resources @ CNAF [status](https://t1metria.cr.cnaf.infn.it/d/QbafK_b7z/resource-usage-per-experiment?orgId=18&var-vo=CYGNO&var-exp=cygn&var-exp_cloud=CYGN)

CYGNO status of usage of [pledged resources](https://monitoring.cloud.infn.it:3000/d/u1sBcydVk/cygno-cloud-capacities?orgId=1)

Moreover, computing resources are available at LNF and LNGS (Cygno VM login and U-LITE nodes) and two [DAQ server](https://drive.google.com/file/d/1kEzvfJK7WSXK2Y1vfEwRqcH9uSmoYsXl/view?usp=sharing) equipped with GPU


### Signup on computing ressources (needed for all resources: CLOUD, LNGS, LNF)
* if you alredy have a **username** INFN please signup in the CYGNO Cloud IAM https://iam-cygno.cloud.cnaf.infn.it/ as **user** ([see INFN Cloud Guide](https://guides.cloud.infn.it/docs/users-guides/en/latest/users_guides/getting_started/getting_started.html)) specifing in the *Notes* field to be part of **cygno-user** group
* if you are not associeted/hosted/employed of INFN plese signup on: https://signup.app.infn.it/ (tips for foreign users see below)
  * accept the security policy  https://userportal.app.infn.it/ (for foreign users no CODICE FISCALE (CF) is needed);
  * follow the traning on computing security;
  * signup in the CYGNO Cloud IAM https://iam-cygno.cloud.cnaf.infn.it/ as **user** ([see INFN Cloud Guide](https://guides.cloud.infn.it/docs/users-guides/en/latest/users_guides/getting_started/getting_started.html)) specifing in the *Notes* field to be part of **cygno-user** group
* if you do not have username in INFN or you get an error (like below) about username plese contact Giovanni Mazzitelli
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/username_error.png" alt="error" style="width:400px;"/> 
<!---
  * for foreign users to be reggistred on AAI you need a CODICE FISCALE (CF) that you can generate with the tool https://quifinanza.it/strumenti/codice-fiscale 
  ```
      (Provincia: “Stato Estero")
      (LUOGO di NASCITA: BRASILE)
  ```
--->
* when approved follow the [HOWTO](https://github.com/CYGNUS-RD/cygno/blob/main/infrastructure.md#usage-of-the-cygno-notebook-web-interface-and-cloud-services) to exploit the resources


### Computing resources and OPEN VPN @ LNF (test DAQ server, ecc)
* send an email to: giovanni.mazzitelli@lnf.infn.it to be autorized
* when aproved install the profile http://www.lnf.infn.it/computing/networking/openvpn-en.php
* if you need also local computing resesources plese fill http://www.lnf.infn.it/computing/cgi-bin/newaccountrequest.pl 

### Computing resources and OPEN VPN @ LNGS (DAQ, shift, ecc)
* send an email to: stefano.piacentini@gssi.it to be autorized
* if you need also local computing resesources **Cygno VM login and U-LITE nodes** (deprecated) plese specify in the mail.
* when aproved install the profile install the profile https://www.lngs.infn.it/en/vpn

### DAQ and Middle Ware ###
* Data are collected by DAQ at LNF and LNGS [server configuration](https://drive.google.com/file/d/1kEzvfJK7WSXK2Y1vfEwRqcH9uSmoYsXl/view?usp=sharing) 
* Exeperiment data are monitored by the quasi-online recostracion by the [Middle Ware](https://github.com/CYGNUS-RD/middleware)

### CYGNO CLOUD Storage
Data collected by the experiment DAQ are automatically pushed on INFN [S3 cloud](https://it.wikipedia.org/wiki/Amazon_S3) storage. The storage data and the experiment area for analysis and simulation can be acces and manage via: 

* Web Tool: https://s3webui.cygno.cloud.infn.it/
* Cloud CYGNO web interfaces tool: https://notebook01.cygno.cloud.infn.it/, https://notebook02.cygno.cloud.infn.it/
* CLI tool: https://github.com/CYGNUS-RD/cygno#cygno-cli-tool-cygno_repo
* 	Analysis: https://s3.cr.cnaf.infn.it:7480/cygno:cygno-analysis/tag/file-name
* 	Data: https://s3.cr.cnaf.infn.it:7480/cygno:cygno-data/tag/file-name
* 	Simulation: https://s3.cr.cnaf.infn.it:7480/cygno:cygno-sim/tag/file-name 

the cloud-storage/ contain tree backet:
* cloud-data: daq stored data, read only
* cloud-sim: simulation input and output data, read and write
* cloud-analysis: analysis input and output data, read and write

### Usage of the CYGNO notebook web interface and Cloud services
Two VM offer acces to cloud infrastrucure via web services based on jupyter notebook interface
* production: 
  - CYGNO notebook 01 https://notebook.cygno.cloud.infn.it/ ([16 CPU](https://novabench.com/parts/cpu/intel-core-broadwell-ibrs)/32 GB); [usage monitor](https://90.147.174.175:3000/login)
  - CYGNO notebook 02 https://notebook02.cygno.cloud.infn.it/ (16 CPU/32 GB);
* test environment https://192.135.24.159/ ([8 CPU](https://www.intel.it/content/www/it/it/products/platforms/details/cascade-lake.html)/16 GB); [usage monitor](https://192.135.24.159:3000)
* the web inteface offer the possibility to run a specific software configuration. In general:
  * tag [dodas](https://github.com/DODAS-TS/dodas-docker-images) realises are the official one and approved by INFN
  * tag [gmazzitelli](https://github.com/gmazzitelli/dodas-docker-images) are realisesed fork of official project our project
### Tag 2.5 ###
Personal Bucket

To set it up:
Go to the storage web browser at: https://s3webui.cygno.cloud.infn.it/. Create a bucket named exactly as your USERNAME (all lowercase), which you can retrieve from a terminal in your notebook by typing: ```echo $USERNAME```

If needed, restart your notebook to enable the changes:
File → Hub Control Panel → Stop Server → Start Server

Optional: If you create a .bashrc file inside your personal bucket, it will be executed at startup, after the global login but before your local folder's .bashrc. This allows for custom startup configurations.
### Tag 2.4 ###
- migration to Ubuntu 22.04.5 LTS, ptyhon 3.11.9
- migration to CNAF storage
- integration of 'cygno_setup' to setup for reco software, GENAT etc, with the specification of CYGNO from CVMFS
- migration to CVMFS storage
- access to CNAF/CLOUD [queue](https://github.com/CYGNUS-RD/mycondor?tab=readme-ov-file#cygno_htc-command-line)
### Tag v1.0.24 ###
 - integration of mango digitizer normailzation files
 - update of the adress for php query
### Tag v1.0.23 ###
 - cygno==v1.0.15
 - ephem==4.1.5
 - iminuit==2.16.0
### Tag v1.0.22 ###
 - Cytron
### Tag v1.0.21 ###
  - fix the INFN IAM bug limiting the access to the condor queue (no short coming are needed now)
  - vim cli editor is available.
### Tag v1.0.20 ###
  - cygno lib v14 (PMT readout)
  - lecroyparser 1.4.2
### Tag v1.0.19 ###
  - cygno lib v10 (PMT readout)
### Tag v1.0.18 ###
  - cygno lib v9 (PMT readout)
  - emacs cli
### Tag v1.0.17 ###
  - python 3.9.10 (not deafult), emacs, screen, root_numpy, uproot, pydot, tensorflow, opencv-python, graphviz
  - [full packege list](https://raw.githubusercontent.com/CYGNUS-RD/cygno/main/requirements.txt)
### Tag < v1.0.17 ###
  - ROOT 6.24/06
  - Python 2/3.6 ([Default package list notebook >= 16](https://raw.githubusercontent.com/CYGNUS-RD/cygno/main/img/PackageListV16.txt))
  - Garfield 
  - GEANT 4.10.5
  - https://gitlab.cern.ch/RooUnfold
  - https://github.com/christopherpoole/CADMesh
  - access to CYGNO cluster (~ 50 cores), condor queues, via the notebook terminal or via any computer by means of [dedicated container](https://github.com/CYGNUS-RD/mycondor)
### Usage:
* to access the resource login with AAI credentials (see above to be athorized) 
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/login.png" alt="login" style="width:400px;"/>
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/aai.png" alt="login" style="width:400px;"/>

* start your notebook choosing version and RAM needed. That RAM is the maximum your interactive job can exploit. if there are concurred interactive job form other users draining the ram you can have your job killed. so don't ask the maximum of RAM if you don't relay need, and use condor queue instead of interactive jobs: https://github.com/CYGNUS-RD/mycondor#cygno-condor-queue 

<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/resorce.png" alt="login" style="width:400px;"/>

* run/edit your notebook Python/ROOT or script via the available buttons
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/buttos.png" alt="login" style="width:400px;"/>

* the file system is availbale at the dafult path **/jupyter-workspace** that is divided in:
  * **/jupyter-workspace/cloud-storage/**: POSIX simulated access to S3 CYGNO storage system (experiment data, simulation and analysis repository, see also [CYGNO cloud storage](https://github.com/CYGNUS-RD/cygno/blob/main/infrastructure.md#cygno-cloud-storage)) 
  * under **/jupyter-workspace/cloud-storage/**: is also available a *USERNAME* directory (accessible only by user) and a *screach* area (accesible by anybody). Those directories are on S3 and permanent.
  * **/jupyter-workspace/private/**: working directory; this access to a local file system in case of cloud fault data can be lost (from v17 this foleder is atomaticaly backuped in **/jupyter-workspace/cloud-storage/USERNAME/private**, safe and always reachbele by [MINIO](https://minio.cloud.infn.it/))
  * **/jupyter-workspace/shared/**: shared working directory on lacal system

* it's strogly sujest to develop and run your code from **/jupyter-workspace/private** use private folder to develop and store your code NOT DATA or OUTPUTs 
* all paths to exploit installed softwares, and condor queues since realese v17, are configured by dafault. A personal setup can be configured editing the file **/jupyter-workspace/cloud-storage/USERNAME/.bashrc** (example git personal config)

# Tips and tricks
## ROOT setup to open ROOT files on cloud from remote
It is possible to remotely open files which are stored on the INFN s3 cloud storage without the need to download them.
For example, from the ROOT prompt line a file can be opened as: 
```
TFile *f= TFile::Open("https://s3.cloud.infn.it/v1/AUTH_2ebf769785574195bde2ff418deac08a/cygno-analysis/RECO/Winter22/reco_run04469_3D.root")
```
To be able to do so, ROOT needs to be configured to read Davix protocols at building time.
To build ROOT from source, follow [ROOT building from source](https://root.cern/install/build_from_source/).
To enable the Davix interface, during the cmake preparation of the build (at the moment 6/10/2023, it is point 3 of the guide just mentioned), add the the options ```-Dbuiltin_davix=ON -Ddavix=ON```.
The command to write from the <builddir> (notation identical to the one used in [ROOT building from source](https://root.cern/install/build_from_source/)) may look something like
```
cmake -DCMAKE_INSTALL_PREFIX=<installdir> -Dbuiltin_davix=ON -Ddavix=ON <sourcedir> 
```
The -Ddavix=ON may not be necessary, but it was not tested without. Any other additional option your specific build may require must be added on the same line.
Continue the ROOT build as described on the provided link and ROOT files will be opened remotely.

If you already have a Davix package installed in your system, it should be enough to just add the ```-Ddavix=ON``` option. However, the printed result of the cmake command must be checked, since cmake looks for a Davix package, but if for any reason a package is not found, it does not raise an error. Thus, the build of ROOT will be successfull, but the user will not be able to open ROOT files from remote.
