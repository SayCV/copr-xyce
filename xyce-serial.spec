Name:               xyce-serial
Version:            6.7
Release:            1%{?dist}
Summary:            Xyce circuit simulator
License:            GPLv3
URL:                https://xyce.sandia.gov

# Source0:          https://xyce.sandia.gov
Source0:            Xyce-%{version}.tar.gz

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:      bison
BuildRequires:      blas-devel
BuildRequires:      cmake
BuildRequires:      fftw-devel
BuildRequires:      flex
BuildRequires:      lapack-devel
BuildRequires:      suitesparse-devel
# BuildRequires:      trilinos-xyce-serial # require fabricesalvaire/xyce
# BuildRequires:    openmpi-devel

Requires:           blas
Requires:           fftw
Requires:           lapack
Requires:           suitesparse
# Requires:         ParMETIS
# Requires:         openmpi

#---------------------------------------------------------------------------------------------------

%description
Xyce is an open source, SPICE-compatible, high-performance analog
circuit simulator, capable of solving extremely large circuit problems
developed at Sandia National Laboratories.

#---------------------------------------------------------------------------------------------------

# Command or series of commands to prepare the software to be built.
%prep
# Xyce-6.7.tar.gz -> Xyce-6.7
%autosetup -n Xyce-%{version}

#---------------------------------------------------------------------------------------------------

%build

configure \
  CXXFLAGS="%{optflags} -O3" \
  ARCHDIR="/usr/local/XyceLibs/Serial" \
  CPPFLAGS="-I/usr/include/suitesparse"

# %make_build
make # don't use -j else it overshoot 8GB of RAM !

#---------------------------------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
%make_install
cd $RPM_BUILD_ROOT
mkdir include/Xyce
mv include/*.h include/Xyce

#---------------------------------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

#---------------------------------------------------------------------------------------------------

%files
%{_bindir}/Xyce
%{_includedir}/ngspice/*
%{_libdir}/libngspice*
%{_libdir}/ngspice/
%{_mandir}/man1/*
%{_datadir}/ngspice/*
%license COPYING

#---------------------------------------------------------------------------------------------------

%changelog
* Sun Sep 17 2017 Fabrice Salvaire <pyspice [AT] fabrice-salvairefedoraproject DOT fr>
- Initial Package for Fedora Copr
