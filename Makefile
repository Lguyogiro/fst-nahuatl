
all: nhi.lexc.hfst

nhi_nnc.lexc.hfst: nhi_nnc.lexc
	hfst-lexc --Werror nhi_nnc.lexc -o nhi_nnc.lexc.hfst

nhi_vnc.lexc.hfst: nhi_vnc.lexc
	hfst-lexc --Werror nhi_vnc.lexc -o nhi_vnc.lexc.hfst

nhi.lexc.hfst: nhi_nnc.lexc.hfst nhi_vnc.lexc.hfst
	hfst-union -1 nhi_nnc.lexc.hfst -2 nhi_vnc.lexc.hfst -o $@

clean:
	rm *.hfst

foma:
	foma -f nhi.foma
