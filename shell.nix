with import <nixpkgs> {
    overlays = [(
        final: prev: {
            pythonPackagesExtensions = prev.pythonPackagesExtensions ++ [(
                python-final: python-prev: {
                    selenium = python-prev.selenium.overridePythonAttrs (oldAttrs: {
                        version = "3.0.0";
                        src = python-prev.fetchPypi {
                            pname = "selenium";
                            version = "3.0.0";
                            hash = "sha256-auf05yjReOIKlOHHKtn2igE87FZJSBT6PlGXg6FyCLc=";
                        };
                        postInstall = null;
                        dontConfigure = true;
                        nativeCheckInputs = [];
                    });
                }
            )];
        }
    )];
};
pkgs.mkShell {
    packages = with pkgs; [
        (python39.withPackages (python-pkgs: with python-pkgs; [
            selenium
        ]))
        chromedriver
        google-chrome
        (pkgs.writeShellScriptBin "google-chrome" "exec -a $0 ${pkgs.google-chrome}/bin/google-chrome-stable $@")
    ];
}
