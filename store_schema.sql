DROP TABLE IF EXISTS customer;
CREATE TABLE customer (
  username        varchar(50) not null PRIMARY KEY,
  password        varchar(50) not null,
  name            varchar(50) not null
);
DROP TABLE IF EXISTS product;
CREATE TABLE product (
  name          varchar(50) not null PRIMARY KEY,
  stock         int(4) not null,
  price         decimal(15,2) not null,
  category      varchar(50) not null,
  description   varchar(1024) not null
);
DROP TABLE IF EXISTS customerOrder;
CREATE TABLE customerOrder (
  id            varchar(50) not null,
  orderNumber   int(4) not null,
  cost          decimal(15,2) not null,
  pdate         date,
  FOREIGN KEY (id) REFERENCES customer(username),
  PRIMARY KEY (id, orderNumber)
);
DROP TABLE IF EXISTS itemsOrdered;
CREATE TABLE itemsOrdered (
  id            varchar(50) not null,
  orderNumber   int(4) not null,
  items         varchar(50),
  quantity      varchar(50),
  cost          decimal(15,2) not null,
  FOREIGN KEY (id) REFERENCES customerOrder(id)
);



INSERT INTO product VALUES ('Omega Seamaster Chronograph', '100', '4900', 'Dive', 'An eye-catching choice within the Diver 300M collection, this unique model features an inner bezel of 18K Sedna™ gold, as well as a black ceramic dial with waves in positive relief, and subdials surrounded by gold.');
INSERT INTO product VALUES ('Rolex Submariner', '100', '9000', 'Dive', 'Launched in 1953, the Submariner was the first divers’ wristwatch waterproof to a depth of 100 metres (330 feet). This was the second great breakthrough in the technical mastery of waterproofness, following the invention of the Oyster, the world’s first waterproof wristwatch, in 1926. In watchmaking, the Submariner represented a historic turning point; it set the standard for divers’ watches. Today, the Submariner is waterproof to a depth of 300 metres (1,000 feet).');
INSERT INTO product VALUES ('Captain Cook', '100', '2750', 'Dive', 'An original look from 1962 is brought to life in a new and improved form for the twenty-first century. With vintage details and styling true to the original, and up-to-date features that make it a match for modern wearers, Captain Cook is a watch designed to stand the test of time. This model features a bronze case as well as a NATO strap made from durable synthetic fabric for a perfect combination of ancient and modern materials.');
INSERT INTO product VALUES ('Doxa Sub 200', '100', '950', 'Dive', 'Unveiled at Baselworld 2019, this 3-hand divers watch has a case made of highest-quality 316L stainless steel. At a diameter of 42 mm, the SUB 200 is topped by a scratch-resistant sapphire crystal with an anti-reflective coating and the distinctive curvature of the domed plexiglass used back in the day. Waterproof to a depth of 200 meters (20 ATM), the model features a unidirectional rotating bezel. All the elements providing dive-relevant information, including the bezel, have a Super‑LumiNova® luminescent coating. The bracelet is 316L stainless steel and features a folding clasp with the DOXA fish symbol.');
INSERT INTO product VALUES ('Cartier Tank', '100', '4000', 'Dress', 'Tank Louis Cartier watch, large model, Manufacture mechanical movement with manual winding, caliber 1917MC. Case in rose gold 750/1000, beaded crown set with a sapphire cabochon, silvered beaded dial, blued-steel sword-shaped hands, mineral crystal, strap in semi-matte brown alligator skin, ardillon buckle in rose gold 750/1000. Case dimensions: 33.7 mm x 25.5 mm, 6.6 mm thick. Water-resistant to 3 bar (30 meters).');
INSERT INTO product VALUES ('Jaeger LeCoultre Reverso', '100', '8750', 'Dress', 'On the front and reverse alike, the Reverso Tribute Duoface watch embodies timelessness with its understated stainless steel case. Echoing the codes of a model dating from the 1930s, it houses a manual winding movement that brings to life its two dials, displaying two time zones and a practical day/night indicator. Its leather strap was specially designed by Casa Fagliano.');
INSERT INTO product VALUES ('Blancpain Villeret Ultraplate', '100', '10000', 'Dress', 'Blancpain’s native village of Villeret lends its name to the most classic collection from the Brand. Firmly anchored in tradition, these models exemplify our roots and embody our prime aesthetic choices. The purity of their lines, the clarity of their dials and the slenderness of their double-stepped cases express essentials with timeless elegance.

The Villeret collection incorporates the results of recent research conducted by Blancpain in the field of movement making. Under-lug correctors, secured calendar and moon phase mechanism, exceptional power reserves: everything possible is done to enhance our timepieces.');
INSERT INTO product VALUES ('PATEK PHILIPPE 5270P PERPETUAL CALENDAR CHRONOGRAPH', '100', '211720', 'Grail', 'Reference 5270, launched in 2011, is heir to several generations of Patek Philippe perpetual calendar chronographs. The Manufacture reinterprets this timepiece in a model featuring an iconic yet original style. The radiance of platinum — the most precious metal of all yet also the hardest to work with — magnifies the timeless design of the case, with its concave bezel, its elegant two-tier lugs and its correction push-pieces that are satin-brushed on the flanks and polished on top.
The perpetual calendar displays are harmoniously arranged, with the date indicated by a hand and a moon phase at 6 o’clock, as well as a twin day/month aperture at 12 o’clock, complemented by two round apertures for the day/night indication and the leap-year cycle. Caliber CH 29-535 PS Q is distinguished by its traditional architecture, combined with six patented innovations relating to the chronograph, as well as by its exceptionally thin calendar mechanism.');
INSERT INTO product VALUES ('AUDEMARS PIGUET ROYAL OAK OPENWORKED GRANDE COMPLICATION', '100', '1477800', 'Grail', 'Combining the 3 categories of horological complications represented by short-time measurement, striking mechanisms and astronomical indications, this model driven by in-house calibre 2885 was hand-crafted by a single master-watchmaker in the Audemars Piguet grande complication workshop.');
INSERT INTO product VALUES ('A. Lange & Söhne Lange 1', '100', '50000', 'Grail', 'It is the classic in the Lange collection. With its inimitable dial design and its outsize date, the LANGE 1 inspired the entire watch industry with fresh impetus. The model version in pink gold features an argenté-coloured dial crafted from solid silver.');


INSERT INTO customer VALUES ('testuser', 'testpass', 'testuser');
-- for testing sort in order history
INSERT INTO customerOrder VALUES('testuser', 1, '3500', '2022-01-02');
INSERT INTO itemsOrdered VALUES('testuser', 1, 'Omega Seamaster Chronograph', '3', '14700');
INSERT INTO customerOrder VALUES('testuser', 2, '3500', '2022-03-21');
INSERT INTO itemsOrdered VALUES('testuser', 2, 'Jaeger LeCoultre Reverso', '1', '14700');
INSERT INTO customerOrder VALUES('testuser', 3, '3500', '2022-03-12');
INSERT INTO itemsOrdered VALUES('testuser', 3, 'Cartier Tank', '3', '14700');
