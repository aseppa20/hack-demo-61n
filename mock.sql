INSERT INTO Ajoneuvot (Rekisteri, Merkki, Malli, Valmistusvuosi, Status) VALUES
('ABC-123', 'Volvo', 'FH16', 2019, 'aktiivinen'),
('DEF-456', 'Scania', 'R580', 2021, 'huollossa'),
('GHI-789', 'Krone', 'CoolLiner', 2018, 'aktiivinen');

INSERT INTO Tulli (vehicle_id, Ylityspaikka, Suunta, Maa, pvm, Tulli_tunnus, Status) VALUES
(1, 'Vaalimaa', 'maastalähtö', 'Viro', '2025-10-01 08:42', 'T20251001A', TRUE),
(2, 'Tornio', 'maahantulo', 'Ruotsi', '2025-10-03 15:27', 'T20251003B', TRUE),
(3, 'Nuijamaa', 'maahantulo', 'Venäjä', '2025-09-29 22:13', 'T20250929C', FALSE);

INSERT INTO Kuljetusyritys (vehicle_id, Kuljettaja, Lähtö, Määränpää, Kuormantyyppi, Lähtöaika, Saapumisaika, Status) VALUES
(1, 'J. Niemi', 'Helsinki', 'Tallinn', 'Elintarvikkeet', '2025-10-01 06:30', '2025-10-01 11:00', 'toimitettu'),
(2, 'A. Korhonen', 'Oulu', 'Tampere', 'Elektroniikka', '2025-10-03 07:15', '2025-10-03 12:45', 'kesken'),
(3, NULL, 'Lappeenranta', 'Pietari', 'Tyhjä perävaunu', '2025-09-29 20:00', '2025-09-29 23:10', 'odottaa');
