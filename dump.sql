--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg100+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.diagnoses DROP CONSTRAINT fk_diagnoses_patient_id_patients;
ALTER TABLE ONLY public.patients DROP CONSTRAINT pk_patients;
ALTER TABLE ONLY public.diagnoses DROP CONSTRAINT pk_diagnoses;
ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
DROP TABLE public.patients;
DROP TABLE public.diagnoses;
DROP TABLE public.alembic_version;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: diagnoses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diagnoses (
    id uuid NOT NULL,
    patient_id uuid NOT NULL,
    status character varying
);


ALTER TABLE public.diagnoses OWNER TO postgres;

--
-- Name: COLUMN diagnoses.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.diagnoses.id IS 'Идентификатор';


--
-- Name: COLUMN diagnoses.patient_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.diagnoses.patient_id IS 'Идентификатор ';


--
-- Name: COLUMN diagnoses.status; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.diagnoses.status IS 'Диагнозы';


--
-- Name: patients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patients (
    id uuid NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    date_of_birth timestamp with time zone NOT NULL
);


ALTER TABLE public.patients OWNER TO postgres;

--
-- Name: COLUMN patients.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.patients.id IS 'Идентификатор';


--
-- Name: COLUMN patients.date_of_birth; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.patients.date_of_birth IS 'Дата рождения';


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
275d172acf7d
\.


--
-- Data for Name: diagnoses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.diagnoses (id, patient_id, status) FROM stdin;
2e061a03-8a9f-4a87-9601-c5e994309305	5695d0fb-a76c-421b-850d-90bd6573ed4d	Умер
0b6b087f-113a-4591-adec-6d764a2cccbb	f579e2a5-2268-4ea4-94fe-a5db554a7765	Болен
297a362a-28ed-434b-80a5-4611682082e7	f579e2a5-2268-4ea4-94fe-a5db554a7765	Почти болен
\.


--
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patients (id, created_at, date_of_birth) FROM stdin;
f579e2a5-2268-4ea4-94fe-a5db554a7765	2022-03-16 19:48:03.683312+03	2022-03-16 19:48:03.683312+03
5695d0fb-a76c-421b-850d-90bd6573ed4d	2022-03-16 20:56:05.0108+03	2022-03-16 20:56:05.0108+03
c59a0dcd-bb76-49f1-a80b-525cbafb2886	2022-03-16 20:56:05.023539+03	2022-03-16 20:56:05.023539+03
a678f21c-2c25-4b28-9081-547c3ab85b5b	2022-03-16 20:56:05.025663+03	2022-03-16 20:56:05.025663+03
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: diagnoses pk_diagnoses; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diagnoses
    ADD CONSTRAINT pk_diagnoses PRIMARY KEY (id);


--
-- Name: patients pk_patients; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT pk_patients PRIMARY KEY (id);


--
-- Name: diagnoses fk_diagnoses_patient_id_patients; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diagnoses
    ADD CONSTRAINT fk_diagnoses_patient_id_patients FOREIGN KEY (patient_id) REFERENCES public.patients(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

