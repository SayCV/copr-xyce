Name:               trilinos-xyce-serial
Version:            12.10.1
Release:            1%{?dist}
Summary:            Trilinos packages for Xyce serial
License:            Trilinos is licensed on a per-package basis. Most packages are now under a BSD license, some are published under the (L)GPL.
URL:                https://trilinos.org

# Source0:          https://trilinos.org/oldsite/download/login.html?tid=tr12101gz
Source0:            https://github.com/trilinos/Trilinos/archive/trilinos-release-%{version}.tar.bz2

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:      bison
BuildRequires:      blas-devel
BuildRequires:      cmake
BuildRequires:      fftw-devel
BuildRequires:      flex
BuildRequires:      lapack-devel
BuildRequires:      suitesparse-devel
# BuildRequires:    openmpi-devel

Requires:           blas
Requires:           fftw
Requires:           lapack
Requires:           suitesparse
# Requires:         ParMETIS
# Requires:         openmpi

#---------------------------------------------------------------------------------------------------

%description
The Trilinos Project is an effort to develop algorithms and enabling
technologies within an object-oriented software framework for the
solution of large-scale, complex multi-physics engineering and
scientific problems. A unique design feature of Trilinos is its focus
on packages.

#---------------------------------------------------------------------------------------------------

# error: Empty %files file /home/fabrice/rpmbuild/BUILD/trilinos-12.10.1-Source/debugfiles.list
%global debug_package %{nil}

#---------------------------------------------------------------------------------------------------

# Command or series of commands to prepare the software to be built.
%prep
# trilinos-release-12-10-1.tar.bz2 -> trilinos-12.10.1-Source
%autosetup -n trilinos-%{version}-Source

#---------------------------------------------------------------------------------------------------

%build

SRCDIR=`pwd`
PREFIX=%{_prefix}/local/XyceLibs/Serial # don't respect FHS
FLAGS="%{optflags} -O3 -fPIC"

mkdir build
cd build

/usr/bin/cmake \
  -G "Unix Makefiles" \
  -DCMAKE_C_COMPILER=gcc \
  -DCMAKE_CXX_COMPILER=g++ \
  -DCMAKE_Fortran_COMPILER=gfortran \
  -DCMAKE_CXX_FLAGS="$FLAGS" \
  -DCMAKE_C_FLAGS="$FLAGS" \
  -DCMAKE_Fortran_FLAGS="$FLAGS" \
  -DCMAKE_INSTALL_PREFIX=$PREFIX \
  -DCMAKE_MAKE_PROGRAM="make" \
  -DTrilinos_ENABLE_NOX=ON \
  -DNOX_ENABLE_LOCA=ON \
  -DTrilinos_ENABLE_EpetraExt=ON \
  -DEpetraExt_BUILD_BTF=ON \
  -DEpetraExt_BUILD_EXPERIMENTAL=ON \
  -DEpetraExt_BUILD_GRAPH_REORDERINGS=ON \
  -DTrilinos_ENABLE_TrilinosCouplings=ON \
  -DTrilinos_ENABLE_Ifpack=ON \
  -DTrilinos_ENABLE_Isorropia=ON \
  -DTrilinos_ENABLE_AztecOO=ON \
  -DTrilinos_ENABLE_Belos=ON \
  -DTrilinos_ENABLE_Teuchos=ON \
  -DTeuchos_ENABLE_COMPLEX=ON \
  -DTrilinos_ENABLE_Amesos=ON \
  -DAmesos_ENABLE_KLU=ON \
  -DAmesos_ENABLE_UMFPACK=ON \
  -DTrilinos_ENABLE_Sacado=ON \
  -DTrilinos_ENABLE_Kokkos=OFF \
  -DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES=OFF \
  -DTPL_ENABLE_AMD=ON \
  -DAMD_LIBRARY_DIRS="/usr/lib" \
  -DTPL_AMD_INCLUDE_DIRS="/usr/include/suitesparse" \
  -DTPL_ENABLE_UMFPACK=ON \
  -DUMFPACK_LIBRARY_DIRS="/usr/lib" \
  -DTPL_UMFPACK_INCLUDE_DIRS="/usr/include/suitesparse" \
  -DTPL_ENABLE_BLAS=ON \
  -DTPL_ENABLE_LAPACK=ON \
  $SRCDIR

%make_build

#---------------------------------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
# %make_install
cd build
make install DESTDIR=%{buildroot}

#---------------------------------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

#---------------------------------------------------------------------------------------------------

%files
# install static libraries !
%{_prefix}/local/XyceLibs/Serial

#---------------------------------------------------------------------------------------------------

%changelog
* Sun Sep 17 2017 Fabrice Salvaire <pyspice [AT] fabrice-salvaire DOT fr>
- Initial Package for Fedora Copr
