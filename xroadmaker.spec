Summary:	XroadMaker
Summary(pl):	XroadMaker
Name:		xroadmaker
Version:	0.5.5
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplicações/Gráficos
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/xroadmaker/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://xroadmaker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	gnome-libs-devel >= 1.0.57
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XRoadMaker is a gnome printed circuit board designer.

%description -l pl
XRoadMaker jest narzêdziem do projektowania p³ytek drukowanych.

%prep
%setup -q
%patch

%build
CXXFLAGS="-Wall %{rpmcflags}"

autoconf
%configure --prefix=%{_prefix}
(cd src; cp -f support_custom.c support.c;cp -f support_custom.h support.h)
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/xroadmaker
%attr(644,root,root) %{_datadir}/%{name}/config/*
%attr(644,root,root) %{_datadir}/%{name}/libs/*

%dir %{_pixmapsdir}/%{name}
%attr(644,root,root) %{_pixmapsdir}/%{name}/*.xpm
