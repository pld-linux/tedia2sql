Summary:	Dia UML Diagram --> SQL Converter
Summary(pl):	Konwerter diagramów UML z DIA do tabel SQL-a
Name:		tedia2sql
Version:	1.2.9
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://tedia2sql.tigris.org/files/documents/282/5625/%{name}-129.tar.gz
# Source0-md5:	1396374395a9c876a5638ecd25139712
Patch0:		%{name}-%{name}rc-home.patch
URL:		http://tedia2sql.tigris.org/
Requires:	dia >= 1:0.90
Requires:	expat >= 1.95.3
Requires:	perl-Digest-MD5
Requires:	perl-XML-DOM
Requires:	perl-XML-Parser
Requires:	perl-XML-RegExp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a tool that allows you to create a database ERD in Dia (using
the UML shape toolset), then to convert that ERD into a SQL DDL script
for multiple databases.

%description -l pl
Narzêdzie s³u¿±ce do konwersji diagramów UML w Dia do skryptów ró¿nych
systemów zarz±dzania bazami danych SQL.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tedia2sql $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "You can find sample configuration file here:"
echo "/usr/share/doc/%{name}-%{version}/tedia2sqlrc.gz"
echo "gunzip it to ~/.tedia2sqlrc and then edit, to cover your needs."
echo

%files
%defattr(644,root,root,755)
%doc README tedia2sqlrc www/*.html www/*.sql www/*.dia
%attr(755,root,root) %{_bindir}/*
