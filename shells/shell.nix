{packages ? import <nixpkgs> {} }:

packages.mkShell {
  buildinputs = with packages; [
    git
    python313
  ];

  pure = true;

  shellHook = ''
    echo "Welcome to nix-craft development environment "
    export PS1="\[\033]2;\h:\u:\w\007\]\n\[\033[1;32m\][\[\e]0;\u@\h: \w\a\]\u@\h(nix-shell):\w]\$\[\033[0m\]"
  '';
}

