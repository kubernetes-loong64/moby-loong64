Name: docker-ce
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Docker Engine (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/moby-loong64
BugURL: https://github.com/kubernetes-loong64/moby-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
Docker Engine (dockerd and docker-proxy) binaries for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 dockerd %{buildroot}/usr/bin/dockerd
install -m 755 docker-proxy %{buildroot}/usr/bin/docker-proxy

mkdir -p %{buildroot}/usr/lib/systemd/system/
install -m 644 systemd/docker.service %{buildroot}/usr/lib/systemd/system/docker.service

mkdir -p %{buildroot}/usr/share/bash-completion/completions/
install -m 644 completions/dockerd.bash %{buildroot}/usr/share/bash-completion/completions/dockerd

mkdir -p %{buildroot}/usr/share/fish/vendor_completions.d/
install -m 644 completions/dockerd.fish %{buildroot}/usr/share/fish/vendor_completions.d/dockerd.fish

mkdir -p %{buildroot}/usr/share/zsh/site-functions/
install -m 644 completions/_dockerd.zsh %{buildroot}/usr/share/zsh/site-functions/_dockerd

mkdir -p %{buildroot}/usr/share/man/man1/
install -m 644 man/dockerd.1 %{buildroot}/usr/share/man/man1/dockerd.1

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/dockerd
/usr/bin/docker-proxy
/usr/lib/systemd/system/docker.service
/usr/share/man/man1/dockerd.1*
/usr/share/bash-completion/completions/dockerd
/usr/share/fish/vendor_completions.d/dockerd.fish
/usr/share/zsh/site-functions/_dockerd

%post
echo "=== docker-ce installed ==="
echo "systemd service file: /usr/lib/systemd/system/docker.service"
echo "Install service:"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable docker.service"
echo "  sudo systemctl start docker.service"

%preun
echo "=== docker-ce uninstalling ==="
echo "Stop and remove service before uninstalling:"
echo "  sudo systemctl stop docker.service 2>/dev/null || true"
echo "  sudo systemctl disable docker.service 2>/dev/null || true"
echo "  sudo rm -f /etc/systemd/system/docker.service"
echo "  sudo systemctl daemon-reload"

%changelog
