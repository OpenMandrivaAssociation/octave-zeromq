%global octpkg zeromq

Summary:	ZeroMQ bindings for GNU Octave
Name:		octave-zeromq
Version:	1.5.6
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/zeromq/
Source0:	https://github.com/gnu-octave/octave-%{octpkg}/releases/download/release-%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	pkgconfig(libzmq)

Requires:	octave(api) = %{octave_api}
Requires:	python%{pyver}dist(pyzmq)

Requires(post): octave
Requires(postun): octave

%description
ZeroMQ bindings for GNU Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

