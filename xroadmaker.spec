Summary:	XroadMaker
Summary(pl):	xroadmaker
Name:		xroadmaker
Version:	0.5.5
Release:	1
Copyright:	GPL
Group:		X11/CAD
Group(pl):	X11/CAD
Source0:	%name-%version.tar.gz
Patch0:		%name-DESTDIR.patch
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	gnome-libs-devel >= 1.0.57
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
Applications/Communications

%description -l pl


%prep
%setup -q

%patch

%build
CXXFLAGS="-Wall $RPM_OTP_FLAGS" \
%configure --prefix=%{_prefix}
(cd src; cp -f support_custom.c support.c;cp -f support_custom.h support.h)
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/xroadmaker
%attr(644,root,root) %{_datadir}/%name/config/*
%attr(644,root,root) %{_datadir}/%name/libs/*

%attr(644,root,root) %{_datadir}/pixmaps/%name/*.xpm
