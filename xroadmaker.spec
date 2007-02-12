Summary:	XroadMaker - printed circuit board designer
Summary(pl.UTF-8):	XroadMaker - program do projektowania płytek drukowanych
Name:		xroadmaker
Version:	0.5.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xroadmaker/%{name}-%{version}.tar.gz
# Source0-md5:	7261fa0c6d55577cbb4ea11bcaa6e1f5
Patch0:		%{name}-DESTDIR.patch
URL:		http://xroadmaker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel >= 1.0.57
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XRoadMaker is a GNOME printed circuit board designer.

%description -l pl.UTF-8
XRoadMaker jest narzędziem do projektowania płytek drukowanych dla
GNOME.

%prep
%setup -q
%patch0 -p1

%build
#CXXFLAGS="-Wall %{rpmcflags}"

%{__autoconf}
%configure
(cd src; cp -f support_custom.c support.c;cp -f support_custom.h support.h)
%{__make}
#RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY README USAGE
%attr(755,root,root) %{_bindir}/xroadmaker
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config
%{_datadir}/%{name}/libs

%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.xpm
