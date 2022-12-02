%global octpkg zeromq

Summary:	ZeroMQ bindings for GNU Octave
Name:		octave-%{octpkg}
Version:	1.5.5
Release:	1
Url:		https://packages.octave.org/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	pkgconfig(libzmq)

Requires:	octave(api) = %{octave_api}
Requires:	python3dist(pyzmq)

Requires(post): octave
Requires(postun): octave

%description
ZeroMQ bindings for GNU Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

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

