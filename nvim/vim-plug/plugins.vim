" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
	
    Plug 'ryanoasis/vim-devicons'
    Plug 'Xuyuanp/nerdtree-git-plugin'
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
    " File Explorer
    Plug 'preservim/nerdtree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " COC 
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Plug 'williamboman/mason.nvim'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'nvim-lualine/lualine.nvim'
    " If you want to have icons in your statusline choose one of these
    Plug 'romgrk/barbar.nvim'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.0' }
    Plug 'Shatur/neovim-ayu'
    Plug 'mhinz/vim-startify'
    Plug 'junegunn/fzf.vim'
    Plug 'uiiaoo/java-syntax.vim'
    Plug 'mcchrish/zenbones.nvim'
    Plug 'rktjmp/lush.nvim'
    Plug 'rebelot/kanagawa.nvim'
    Plug 'projekt0n/github-nvim-theme'
    Plug 'agude/vim-eldar'
    Plug 'morhetz/gruvbox'
call plug#end()
