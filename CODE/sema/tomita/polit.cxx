#encoding "utf8"
PolitName -> Word<kwtype=politiki>;

Polit -> PolitName interp (Polit.Name);


Text -> AnyWord* Polit AnyWord*;
Text2 -> Text interp (Polit.Text);
