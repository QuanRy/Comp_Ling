#encoding "utf8"

PlaceName -> Word<kwtype=dostopr>;

Place -> PlaceName interp (Place.Name);


Text -> AnyWord* Place AnyWord*;
Text2 -> Text interp (Place.Text);


