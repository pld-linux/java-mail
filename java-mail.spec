Summary: 	JavaMail - Java mail system
Summary(pl):	JavaMail - system pocztowy w Javie
Name:		javamail
Version:	1.2
Release:	1
License:	Read LICENSE.txt!
Group:		Development/Languages/Java
Source0:	javamail-1_2.zip
URL:		http://java.sun.com/products/javamail/
Requires:	jaf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
The JavaMail(TM) API provides a set of abstract classes that model a
mail system. The API provides a platform independent and protocol
independent framework to build Java technology-based mail and
messaging applications.

%description -l pl
API JavaMail(TM) daje zestaw klas abstrakcyjnych tworz±cych system
pocztowy. API daje niezale¿ne od platformy i protoko³u ¶rodowisko do
tworzenia aplikacji pocztowych i komunikacyjnych w oparciu o Javê.

%package doc
Summary:	JavaMail documentation
Summary(pl):	Dokumentacja do JavaMail
Group:		Development/Languages/Java

%description doc
JavaMail documentation.

%description doc -l pl
Dokumentacja do JavaMail.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf CHANGES.txt LICENSE.txt NOTES.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
