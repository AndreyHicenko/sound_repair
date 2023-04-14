--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-04-14 20:57:28

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16414)
-- Name: table_admin_id; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_admin_id (
    id_admin_users numeric(15,0),
    admin_lost_message text
);


ALTER TABLE public.table_admin_id OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16409)
-- Name: table_price_amplifier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_price_amplifier (
    type_work text,
    price integer
);


ALTER TABLE public.table_price_amplifier OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16399)
-- Name: table_price_dinamic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_price_dinamic (
    type_work text,
    price integer
);


ALTER TABLE public.table_price_dinamic OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16404)
-- Name: table_price_subwoofer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_price_subwoofer (
    type_work text,
    price integer
);


ALTER TABLE public.table_price_subwoofer OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16420)
-- Name: table_users_id; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_users_id (
    id_users numeric(15,0)
);


ALTER TABLE public.table_users_id OWNER TO postgres;

--
-- TOC entry 3333 (class 0 OID 16414)
-- Dependencies: 217
-- Data for Name: table_admin_id; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_admin_id (id_admin_users, admin_lost_message) FROM stdin;
\.


--
-- TOC entry 3332 (class 0 OID 16409)
-- Dependencies: 216
-- Data for Name: table_price_amplifier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_price_amplifier (type_work, price) FROM stdin;
Замена RCA гнезда AB класс	400
Замена переключателя hpf и lpf AB класс	400
Замена терминала AB класс	600
Замена диэлектрических подложек AB класс	500
Работа AB класс	500
Работа D класс	1500
Замена RCA гнезда D класс	600
Замена переключателя hpf и lpf D класс	600
Замена терминала D класс	700
Замена диэлектрических подложек D класс	700
\.


--
-- TOC entry 3330 (class 0 OID 16399)
-- Dependencies: 214
-- Data for Name: table_price_dinamic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_price_dinamic (type_work, price) FROM stdin;
Замена катушки 1 дюйм на динамики	600
Замена катушки 1,5 дюйма на динамики	700
Замена катушки 2 дюйма на динамике	800
Замена катушки 3 дюйма на динамики	900
Замена катушки 4 дюйма на динамики	1500
Замена диффузора на динамике 16см	500
Замена диффузора на динамике 20см	700
Замена диффузора на динамике 25см	700
Замена диффузора на динамике 30см	1000
Замена диффузора на динамике 38см	1200
Замена диффузора на динамике 46см	1500
\.


--
-- TOC entry 3331 (class 0 OID 16404)
-- Dependencies: 215
-- Data for Name: table_price_subwoofer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_price_subwoofer (type_work, price) FROM stdin;
Замена катушки на сабвуфере	800
Замена диффузора на сабвуфере	500
Замена колпака	100
Замена подводящих с запчастью	600
Замена центрующих шайб	500
Установка нашего прижимного кольца	400
\.


--
-- TOC entry 3334 (class 0 OID 16420)
-- Dependencies: 218
-- Data for Name: table_users_id; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_users_id (id_users) FROM stdin;
5673151625
6186779086
\.


-- Completed on 2023-04-14 20:57:29

--
-- PostgreSQL database dump complete
--

