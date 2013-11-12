--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: adjuntos; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE adjuntos (
    id integer NOT NULL,
    mensaje_id integer NOT NULL,
    archivo character varying(100)
);


ALTER TABLE public.adjuntos OWNER TO umail;

--
-- Name: adjuntos_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE adjuntos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adjuntos_id_seq OWNER TO umail;

--
-- Name: adjuntos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE adjuntos_id_seq OWNED BY adjuntos.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO umail;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO umail;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO umail;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO umail;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO umail;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO umail;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_pregunta; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_pregunta (
    id integer NOT NULL,
    opcion character varying(50) NOT NULL
);


ALTER TABLE public.auth_pregunta OWNER TO umail;

--
-- Name: auth_pregunta_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_pregunta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_pregunta_id_seq OWNER TO umail;

--
-- Name: auth_pregunta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_pregunta_id_seq OWNED BY auth_pregunta.id;


--
-- Name: auth_preguntassecretas; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_preguntassecretas (
    id integer NOT NULL,
    pregunta_id integer NOT NULL,
    respuesta character varying(300) NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.auth_preguntassecretas OWNER TO umail;

--
-- Name: auth_preguntassecretas_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_preguntassecretas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_preguntassecretas_id_seq OWNER TO umail;

--
-- Name: auth_preguntassecretas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_preguntassecretas_id_seq OWNED BY auth_preguntassecretas.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(250) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO umail;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO umail;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO umail;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO umail;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO umail;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO umail;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: auth_userprofile; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE auth_userprofile (
    id integer NOT NULL,
    user_id integer NOT NULL,
    persona_id integer NOT NULL,
    notificaciones boolean NOT NULL
);


ALTER TABLE public.auth_userprofile OWNER TO umail;

--
-- Name: auth_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE auth_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_userprofile_id_seq OWNER TO umail;

--
-- Name: auth_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE auth_userprofile_id_seq OWNED BY auth_userprofile.id;


--
-- Name: comentarios; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE comentarios (
    id integer NOT NULL,
    pregunta character varying(50) NOT NULL,
    comentario text NOT NULL,
    nombre character varying(50) NOT NULL,
    correo character varying(75) NOT NULL
);


ALTER TABLE public.comentarios OWNER TO umail;

--
-- Name: comentarios_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE comentarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comentarios_id_seq OWNER TO umail;

--
-- Name: comentarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE comentarios_id_seq OWNED BY comentarios.id;


--
-- Name: dependencias; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE dependencias (
    id integer NOT NULL,
    ubicacion_id integer NOT NULL,
    tipo_sede_id integer NOT NULL,
    departamento character varying(50) NOT NULL,
    siglas character varying(50) NOT NULL,
    telefono integer,
    nivel_id integer NOT NULL,
    dependencia_id integer,
    cargo_max_id integer
);


ALTER TABLE public.dependencias OWNER TO umail;

--
-- Name: dependencias_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE dependencias_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dependencias_id_seq OWNER TO umail;

--
-- Name: dependencias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE dependencias_id_seq OWNED BY dependencias.id;


--
-- Name: destinatarios; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE destinatarios (
    id integer NOT NULL,
    grupos_id integer,
    usuarios_id integer
);


ALTER TABLE public.destinatarios OWNER TO umail;

--
-- Name: destinatarios_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE destinatarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.destinatarios_id_seq OWNER TO umail;

--
-- Name: destinatarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE destinatarios_id_seq OWNED BY destinatarios.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO umail;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO umail;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO umail;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO umail;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_messages_estadomemo; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_messages_estadomemo (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.django_messages_estadomemo OWNER TO umail;

--
-- Name: django_messages_estadomemo_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_messages_estadomemo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_messages_estadomemo_id_seq OWNER TO umail;

--
-- Name: django_messages_estadomemo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_messages_estadomemo_id_seq OWNED BY django_messages_estadomemo.id;


--
-- Name: django_messages_estadomemo_modificable; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_messages_estadomemo_modificable (
    id integer NOT NULL,
    estadomemo_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.django_messages_estadomemo_modificable OWNER TO umail;

--
-- Name: django_messages_estadomemo_modificable_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_messages_estadomemo_modificable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_messages_estadomemo_modificable_id_seq OWNER TO umail;

--
-- Name: django_messages_estadomemo_modificable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_messages_estadomemo_modificable_id_seq OWNED BY django_messages_estadomemo_modificable.id;


--
-- Name: django_messages_message; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_messages_message (
    id integer NOT NULL,
    recipient_id integer,
    con_copia boolean NOT NULL,
    subject character varying(255),
    archivo character varying(100),
    body text,
    sender_id integer NOT NULL,
    parent_msg_id integer,
    sent_at timestamp with time zone,
    read_at timestamp with time zone,
    replied_at timestamp with time zone,
    deleted_at timestamp with time zone,
    status_id integer,
    tipo character varying(10),
    codigo character varying(30),
    num_ident bigint,
    borrador boolean NOT NULL
);


ALTER TABLE public.django_messages_message OWNER TO umail;

--
-- Name: django_messages_message_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_messages_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_messages_message_id_seq OWNER TO umail;

--
-- Name: django_messages_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_messages_message_id_seq OWNED BY django_messages_message.id;


--
-- Name: django_select2_keymap; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_select2_keymap (
    id integer NOT NULL,
    key character varying(40) NOT NULL,
    value character varying(100) NOT NULL,
    accessed_on timestamp with time zone NOT NULL
);


ALTER TABLE public.django_select2_keymap OWNER TO umail;

--
-- Name: django_select2_keymap_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_select2_keymap_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_select2_keymap_id_seq OWNER TO umail;

--
-- Name: django_select2_keymap_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_select2_keymap_id_seq OWNED BY django_select2_keymap.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO umail;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO umail;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO umail;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: estado; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE estado (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    pais_id integer NOT NULL
);


ALTER TABLE public.estado OWNER TO umail;

--
-- Name: estado_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE estado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_id_seq OWNER TO umail;

--
-- Name: estado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE estado_id_seq OWNED BY estado.id;


--
-- Name: filer_clipboard; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_clipboard (
    id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.filer_clipboard OWNER TO umail;

--
-- Name: filer_clipboard_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE filer_clipboard_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filer_clipboard_id_seq OWNER TO umail;

--
-- Name: filer_clipboard_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE filer_clipboard_id_seq OWNED BY filer_clipboard.id;


--
-- Name: filer_clipboarditem; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_clipboarditem (
    id integer NOT NULL,
    file_id integer NOT NULL,
    clipboard_id integer NOT NULL
);


ALTER TABLE public.filer_clipboarditem OWNER TO umail;

--
-- Name: filer_clipboarditem_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE filer_clipboarditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filer_clipboarditem_id_seq OWNER TO umail;

--
-- Name: filer_clipboarditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE filer_clipboarditem_id_seq OWNED BY filer_clipboarditem.id;


--
-- Name: filer_file; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_file (
    id integer NOT NULL,
    polymorphic_ctype_id integer,
    folder_id integer,
    file character varying(255),
    _file_size integer,
    sha1 character varying(40) NOT NULL,
    has_all_mandatory_data boolean NOT NULL,
    original_filename character varying(255),
    name character varying(255) NOT NULL,
    description text,
    owner_id integer,
    uploaded_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_public boolean NOT NULL
);


ALTER TABLE public.filer_file OWNER TO umail;

--
-- Name: filer_file_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE filer_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filer_file_id_seq OWNER TO umail;

--
-- Name: filer_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE filer_file_id_seq OWNED BY filer_file.id;


--
-- Name: filer_folder; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_folder (
    id integer NOT NULL,
    parent_id integer,
    name character varying(255) NOT NULL,
    owner_id integer,
    uploaded_at timestamp with time zone NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    CONSTRAINT filer_folder_level_check CHECK ((level >= 0)),
    CONSTRAINT filer_folder_lft_check CHECK ((lft >= 0)),
    CONSTRAINT filer_folder_rght_check CHECK ((rght >= 0)),
    CONSTRAINT filer_folder_tree_id_check CHECK ((tree_id >= 0))
);


ALTER TABLE public.filer_folder OWNER TO umail;

--
-- Name: filer_folder_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE filer_folder_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filer_folder_id_seq OWNER TO umail;

--
-- Name: filer_folder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE filer_folder_id_seq OWNED BY filer_folder.id;


--
-- Name: filer_folderpermission; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_folderpermission (
    id integer NOT NULL,
    folder_id integer,
    type smallint NOT NULL,
    user_id integer,
    group_id integer,
    everybody boolean NOT NULL,
    can_edit smallint,
    can_read smallint,
    can_add_children smallint
);


ALTER TABLE public.filer_folderpermission OWNER TO umail;

--
-- Name: filer_folderpermission_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE filer_folderpermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filer_folderpermission_id_seq OWNER TO umail;

--
-- Name: filer_folderpermission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE filer_folderpermission_id_seq OWNED BY filer_folderpermission.id;


--
-- Name: filer_image; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE filer_image (
    file_ptr_id integer NOT NULL,
    _height integer,
    _width integer,
    date_taken timestamp with time zone,
    default_alt_text character varying(255),
    default_caption character varying(255),
    author character varying(255),
    must_always_publish_author_credit boolean NOT NULL,
    must_always_publish_copyright boolean NOT NULL,
    subject_location character varying(64)
);


ALTER TABLE public.filer_image OWNER TO umail;

--
-- Name: manual_usuario; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE manual_usuario (
    id integer NOT NULL,
    titulo character varying(100) NOT NULL,
    seccion character varying(15) NOT NULL
);


ALTER TABLE public.manual_usuario OWNER TO umail;

--
-- Name: manual_usuario_detalles; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE manual_usuario_detalles (
    id integer NOT NULL,
    manual_id integer NOT NULL,
    texto text NOT NULL,
    imagen character varying(100) NOT NULL
);


ALTER TABLE public.manual_usuario_detalles OWNER TO umail;

--
-- Name: manual_usuario_detalles_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE manual_usuario_detalles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.manual_usuario_detalles_id_seq OWNER TO umail;

--
-- Name: manual_usuario_detalles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE manual_usuario_detalles_id_seq OWNED BY manual_usuario_detalles.id;


--
-- Name: manual_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE manual_usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.manual_usuario_id_seq OWNER TO umail;

--
-- Name: manual_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE manual_usuario_id_seq OWNED BY manual_usuario.id;


--
-- Name: municipio; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE municipio (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    estado_id integer NOT NULL
);


ALTER TABLE public.municipio OWNER TO umail;

--
-- Name: municipio_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE municipio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.municipio_id_seq OWNER TO umail;

--
-- Name: municipio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE municipio_id_seq OWNED BY municipio.id;


--
-- Name: niveles; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE niveles (
    id integer NOT NULL,
    numero integer NOT NULL
);


ALTER TABLE public.niveles OWNER TO umail;

--
-- Name: niveles_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE niveles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.niveles_id_seq OWNER TO umail;

--
-- Name: niveles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE niveles_id_seq OWNED BY niveles.id;


--
-- Name: noticias; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE noticias (
    id integer NOT NULL,
    titulo character varying(300) NOT NULL,
    texto text NOT NULL,
    fecha timestamp with time zone NOT NULL
);


ALTER TABLE public.noticias OWNER TO umail;

--
-- Name: noticias_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE noticias_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.noticias_id_seq OWNER TO umail;

--
-- Name: noticias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE noticias_id_seq OWNED BY noticias.id;


--
-- Name: pais; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE pais (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.pais OWNER TO umail;

--
-- Name: pais_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE pais_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pais_id_seq OWNER TO umail;

--
-- Name: pais_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE pais_id_seq OWNED BY pais.id;


--
-- Name: parroquia; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE parroquia (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    municipio_id integer NOT NULL
);


ALTER TABLE public.parroquia OWNER TO umail;

--
-- Name: parroquia_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE parroquia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parroquia_id_seq OWNER TO umail;

--
-- Name: parroquia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE parroquia_id_seq OWNED BY parroquia.id;


--
-- Name: personal; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE personal (
    id integer NOT NULL,
    tipo_personal_id integer NOT NULL,
    dependencia_id integer NOT NULL,
    cargo_id integer NOT NULL
);


ALTER TABLE public.personal OWNER TO umail;

--
-- Name: personal_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE personal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personal_id_seq OWNER TO umail;

--
-- Name: personal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE personal_id_seq OWNED BY personal.id;


--
-- Name: personas; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE personas (
    id integer NOT NULL,
    tipodoc character varying(1) NOT NULL,
    num_identificacion character varying(50) NOT NULL,
    primer_apellido character varying(100) NOT NULL,
    segundo_apellido character varying(100) NOT NULL,
    primer_nombre character varying(100) NOT NULL,
    segundo_nombre character varying(100) NOT NULL,
    genero integer NOT NULL,
    email character varying(75) NOT NULL,
    telefono character varying(15),
    cargo_principal_id integer NOT NULL
);


ALTER TABLE public.personas OWNER TO umail;

--
-- Name: personas_cargos_autorizados; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE personas_cargos_autorizados (
    id integer NOT NULL,
    personas_id integer NOT NULL,
    personal_id integer NOT NULL
);


ALTER TABLE public.personas_cargos_autorizados OWNER TO umail;

--
-- Name: personas_cargos_autorizados_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE personas_cargos_autorizados_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personas_cargos_autorizados_id_seq OWNER TO umail;

--
-- Name: personas_cargos_autorizados_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE personas_cargos_autorizados_id_seq OWNED BY personas_cargos_autorizados.id;


--
-- Name: personas_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE personas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personas_id_seq OWNER TO umail;

--
-- Name: personas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE personas_id_seq OWNED BY personas.id;


--
-- Name: respuestas; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE respuestas (
    id integer NOT NULL,
    pregunta_id integer NOT NULL,
    comentario text NOT NULL,
    usuario_id integer,
    respondido boolean NOT NULL
);


ALTER TABLE public.respuestas OWNER TO umail;

--
-- Name: respuestas_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE respuestas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.respuestas_id_seq OWNER TO umail;

--
-- Name: respuestas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE respuestas_id_seq OWNED BY respuestas.id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO umail;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO umail;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: tipo_personal; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE tipo_personal (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.tipo_personal OWNER TO umail;

--
-- Name: tipo_personal_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE tipo_personal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_personal_id_seq OWNER TO umail;

--
-- Name: tipo_personal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE tipo_personal_id_seq OWNED BY tipo_personal.id;


--
-- Name: tipo_sede; Type: TABLE; Schema: public; Owner: umail; Tablespace: 
--

CREATE TABLE tipo_sede (
    id integer NOT NULL,
    nombre character varying(20) NOT NULL
);


ALTER TABLE public.tipo_sede OWNER TO umail;

--
-- Name: tipo_sede_id_seq; Type: SEQUENCE; Schema: public; Owner: umail
--

CREATE SEQUENCE tipo_sede_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_sede_id_seq OWNER TO umail;

--
-- Name: tipo_sede_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umail
--

ALTER SEQUENCE tipo_sede_id_seq OWNED BY tipo_sede.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY adjuntos ALTER COLUMN id SET DEFAULT nextval('adjuntos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_pregunta ALTER COLUMN id SET DEFAULT nextval('auth_pregunta_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_preguntassecretas ALTER COLUMN id SET DEFAULT nextval('auth_preguntassecretas_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_userprofile ALTER COLUMN id SET DEFAULT nextval('auth_userprofile_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY comentarios ALTER COLUMN id SET DEFAULT nextval('comentarios_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias ALTER COLUMN id SET DEFAULT nextval('dependencias_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY destinatarios ALTER COLUMN id SET DEFAULT nextval('destinatarios_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_estadomemo ALTER COLUMN id SET DEFAULT nextval('django_messages_estadomemo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_estadomemo_modificable ALTER COLUMN id SET DEFAULT nextval('django_messages_estadomemo_modificable_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_message ALTER COLUMN id SET DEFAULT nextval('django_messages_message_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_select2_keymap ALTER COLUMN id SET DEFAULT nextval('django_select2_keymap_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY estado ALTER COLUMN id SET DEFAULT nextval('estado_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_clipboard ALTER COLUMN id SET DEFAULT nextval('filer_clipboard_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_clipboarditem ALTER COLUMN id SET DEFAULT nextval('filer_clipboarditem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_file ALTER COLUMN id SET DEFAULT nextval('filer_file_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folder ALTER COLUMN id SET DEFAULT nextval('filer_folder_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folderpermission ALTER COLUMN id SET DEFAULT nextval('filer_folderpermission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY manual_usuario ALTER COLUMN id SET DEFAULT nextval('manual_usuario_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY manual_usuario_detalles ALTER COLUMN id SET DEFAULT nextval('manual_usuario_detalles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY municipio ALTER COLUMN id SET DEFAULT nextval('municipio_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY niveles ALTER COLUMN id SET DEFAULT nextval('niveles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY noticias ALTER COLUMN id SET DEFAULT nextval('noticias_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY pais ALTER COLUMN id SET DEFAULT nextval('pais_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY parroquia ALTER COLUMN id SET DEFAULT nextval('parroquia_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personal ALTER COLUMN id SET DEFAULT nextval('personal_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personas ALTER COLUMN id SET DEFAULT nextval('personas_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personas_cargos_autorizados ALTER COLUMN id SET DEFAULT nextval('personas_cargos_autorizados_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY respuestas ALTER COLUMN id SET DEFAULT nextval('respuestas_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY tipo_personal ALTER COLUMN id SET DEFAULT nextval('tipo_personal_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: umail
--

ALTER TABLE ONLY tipo_sede ALTER COLUMN id SET DEFAULT nextval('tipo_sede_id_seq'::regclass);


--
-- Data for Name: adjuntos; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY adjuntos (id, mensaje_id, archivo) FROM stdin;
\.


--
-- Name: adjuntos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('adjuntos_id_seq', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_group (id, name) FROM stdin;
1	Rector(a)
2	Decano(a)
4	DIrector(a)
5	Secretaria
6	Programador(a)
3	Coordinador(a)
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_group_id_seq', 6, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
49	1	49
50	1	50
51	1	51
52	1	52
53	1	53
54	1	54
55	1	55
56	1	56
57	1	57
58	1	58
59	1	59
60	1	60
61	1	61
62	1	62
63	1	63
64	1	64
65	1	65
66	1	66
67	1	67
68	1	68
69	1	69
70	1	70
71	1	71
72	1	72
73	1	73
74	1	74
75	1	75
76	1	76
77	1	77
78	1	78
79	1	79
80	1	80
81	1	81
82	1	82
83	1	83
84	1	84
85	1	85
86	1	86
87	1	87
88	1	88
89	1	89
90	1	90
91	1	91
92	1	92
93	1	93
94	1	94
95	1	95
96	1	96
97	1	97
98	1	98
99	1	99
100	1	100
101	1	101
102	1	102
103	1	103
104	1	104
105	1	105
106	1	106
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 106, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add pregunta	4	add_pregunta
11	Can change pregunta	4	change_pregunta
12	Can delete pregunta	4	delete_pregunta
13	Can add Pregunta secreta	5	add_preguntassecretas
14	Can change Pregunta secreta	5	change_preguntassecretas
15	Can delete Pregunta secreta	5	delete_preguntassecretas
16	Can add Usuario	6	add_userprofile
17	Can change Usuario	6	change_userprofile
18	Can delete Usuario	6	delete_userprofile
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add content type	8	add_contenttype
23	Can change content type	8	change_contenttype
24	Can delete content type	8	delete_contenttype
25	Can add session	9	add_session
26	Can change session	9	change_session
27	Can delete session	9	delete_session
28	Can add site	10	add_site
29	Can change site	10	change_site
30	Can delete site	10	delete_site
31	Can add destinatario	11	add_destinatarios
32	Can change destinatario	11	change_destinatarios
33	Can delete destinatario	11	delete_destinatarios
34	Can add estado memo	12	add_estadomemo
35	Can change estado memo	12	change_estadomemo
36	Can delete estado memo	12	delete_estadomemo
37	Can add adjunto	13	add_adjunto
38	Can change adjunto	13	change_adjunto
39	Can delete adjunto	13	delete_adjunto
40	Can add Message	14	add_message
41	Can change Message	14	change_message
42	Can delete Message	14	delete_message
43	Can add personas	15	add_personas
44	Can change personas	15	change_personas
45	Can delete personas	15	delete_personas
46	Can add personal	16	add_personal
47	Can change personal	16	change_personal
48	Can delete personal	16	delete_personal
49	Can add tipo de personal	17	add_tipopersonal
50	Can change tipo de personal	17	change_tipopersonal
51	Can delete tipo de personal	17	delete_tipopersonal
52	Can add dependencia	18	add_dependencias
53	Can change dependencia	18	change_dependencias
54	Can delete dependencia	18	delete_dependencias
55	Can add tipo de sede	19	add_tiposede
56	Can change tipo de sede	19	change_tiposede
57	Can delete tipo de sede	19	delete_tiposede
58	Can add nivel	20	add_niveles
59	Can change nivel	20	change_niveles
60	Can delete nivel	20	delete_niveles
61	Can add parroquia	21	add_parroquias
62	Can change parroquia	21	change_parroquias
63	Can delete parroquia	21	delete_parroquias
64	Can add municipio	22	add_municipio
65	Can change municipio	22	change_municipio
66	Can delete municipio	22	delete_municipio
67	Can add estado	23	add_estado
68	Can change estado	23	change_estado
69	Can delete estado	23	delete_estado
70	Can add país	24	add_pais
71	Can change país	24	change_pais
72	Can delete país	24	delete_pais
73	Can add noticias	25	add_noticias
74	Can change noticias	25	change_noticias
75	Can delete noticias	25	delete_noticias
76	Can add comentarios	26	add_comentarios
77	Can change comentarios	26	change_comentarios
78	Can delete comentarios	26	delete_comentarios
79	Can add manual_ detalles	27	add_manual_detalles
80	Can change manual_ detalles	27	change_manual_detalles
81	Can delete manual_ detalles	27	delete_manual_detalles
82	Can add manual	28	add_manual
83	Can change manual	28	change_manual
84	Can delete manual	28	delete_manual
85	Can add key map	29	add_keymap
86	Can change key map	29	change_keymap
87	Can delete key map	29	delete_keymap
88	Can add Folder	30	add_folder
89	Can change Folder	30	change_folder
90	Can delete Folder	30	delete_folder
91	Can use directory listing	30	can_use_directory_listing
92	Can add folder permission	31	add_folderpermission
93	Can change folder permission	31	change_folderpermission
94	Can delete folder permission	31	delete_folderpermission
95	Can add file	32	add_file
96	Can change file	32	change_file
97	Can delete file	32	delete_file
98	Can add clipboard	33	add_clipboard
99	Can change clipboard	33	change_clipboard
100	Can delete clipboard	33	delete_clipboard
101	Can add clipboard item	34	add_clipboarditem
102	Can change clipboard item	34	change_clipboarditem
103	Can delete clipboard item	34	delete_clipboarditem
104	Can add image	35	add_image
105	Can change image	35	change_image
106	Can delete image	35	delete_image
107	Can add respuestas	36	add_respuestas
108	Can change respuestas	36	change_respuestas
109	Can delete respuestas	36	delete_respuestas
110	Can add migration history	37	add_migrationhistory
111	Can change migration history	37	change_migrationhistory
112	Can delete migration history	37	delete_migrationhistory
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_permission_id_seq', 112, true);


--
-- Data for Name: auth_pregunta; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_pregunta (id, opcion) FROM stdin;
1	Segundo apellido de su abuelo/a
2	Nombre de su primera mascota
3	Nombre de su primer/a novio/a
4	Segundo nombre de su hermano/a mayor
5	Cuál es su número de calzado
6	Su primer número telefónico
7	Lugar de nacimiento de su primer/a hijo/a
8	Año de nacimiento de su madre
9	Año de nacimiento de su padre
10	Nombre de su plato favorito de comida
11	Marca de automóviles preferidos
12	Nombre de su profesor/a favorito/a
13	Pasatiempo favorito
14	Animal favorito
15	Color favorito
\.


--
-- Name: auth_pregunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_pregunta_id_seq', 15, true);


--
-- Data for Name: auth_preguntassecretas; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_preguntassecretas (id, pregunta_id, respuesta, usuario_id) FROM stdin;
\.


--
-- Name: auth_preguntassecretas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_preguntassecretas_id_seq', 1, false);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$10000$ik7u7xVbkf5o$p8sYaiShAnatOnvJ3LiSew7WR9fqNNCOkJpI0zalaVE=	2013-09-19 20:39:22.667701-04:30	f	arod.unerg@gmail.com	Alberto	Rodríguez	arod.unerg@gmail.com	t	t	2013-09-19 20:39:22.667701-04:30
2	pbkdf2_sha256$10000$HUb5qhmAP12y$7kE6oP7bfNis144ThVMx5kZyWdFauVgbra0YyN7XL9E=	2013-09-19 20:26:47.460493-04:30	f	mariadepalm@udefa.edu.ve	María	Medina	mariadepalm@udefa.edu.ve	t	t	2013-09-19 20:26:47.460493-04:30
5	pbkdf2_sha256$10000$17Q5wLIxaiVu$LTA68Wnp4Lxde5AcDSS0tpYm2LjSVHOZubSmfJiNZhk=	2013-09-21 15:34:37.975768-04:30	f	edgaropalomaresm@gmail.com	Edgar	Palomares	edgaropalomaresm@gmail.com	t	t	2013-09-21 15:34:37.975768-04:30
6	pbkdf2_sha256$10000$nsgYCx2VzdrG$YJqPLyuVecnLWdIdsC0Hi7YiUxgOurNIfMry1KbeUSY=	2013-09-21 16:54:58.025663-04:30	f	mrgc71@gmail.com	Miguel	González	mrgc71@gmail.com	t	t	2013-09-21 16:54:58.025663-04:30
1	pbkdf2_sha256$10000$Zhw812VMS8k5$6UZoBIxP9VEiYkIOA2WwGszRVnIcRqQiHZDp5YbEIOk=	2013-10-02 17:51:08.267969-04:30	t	f0ry	Jennifer	Montilla	montilla.jennifer@gmail.com	t	t	2013-09-19 19:57:17-04:30
4	pbkdf2_sha256$10000$2IR7wGKMYuxV$T/LdDpC1B5M20XXXFfqYWvk7lBicNXd+R7kwAOhy5F4=	2013-10-07 01:23:54.853962-04:30	t	axelio	Axel	Díaz	correo@correo.com	t	t	2013-09-20 11:12:51.21971-04:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
2	3	2
3	5	3
5	6	4
6	4	5
7	1	5
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 7, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_user_id_seq', 7, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: auth_userprofile; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY auth_userprofile (id, user_id, persona_id, notificaciones) FROM stdin;
1	2	1	f
2	3	2	f
3	5	3	f
4	1	4	f
5	6	5	f
7	4	6	f
\.


--
-- Name: auth_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('auth_userprofile_id_seq', 8, true);


--
-- Data for Name: comentarios; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY comentarios (id, pregunta, comentario, nombre, correo) FROM stdin;
\.


--
-- Name: comentarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('comentarios_id_seq', 1, false);


--
-- Data for Name: dependencias; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY dependencias (id, ubicacion_id, tipo_sede_id, departamento, siglas, telefono, nivel_id, dependencia_id, cargo_max_id) FROM stdin;
1	1	2	Rectorado	R	\N	1	\N	1
3	1	1	Área de Ingeniería en Sistemas	AIS	\N	2	1	2
6	1	1	Dirección de Informática	DI	\N	5	5	4
5	1	1	Secretaría	S	\N	3	1	5
4	1	1	Dirección de Admisión, Control y Evaluación	DACE	\N	3	1	4
\.


--
-- Name: dependencias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('dependencias_id_seq', 6, true);


--
-- Data for Name: destinatarios; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY destinatarios (id, grupos_id, usuarios_id) FROM stdin;
1	1	\N
2	\N	1
3	2	\N
4	3	\N
5	\N	2
6	4	\N
7	\N	3
8	5	\N
9	6	\N
10	\N	4
11	\N	5
12	\N	7
\.


--
-- Name: destinatarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('destinatarios_id_seq', 12, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2013-09-19 20:09:23.35476-04:30	1	17	1	Académico	1	
2	2013-09-19 20:09:34.888081-04:30	1	17	2	Obrero	1	
3	2013-09-19 20:09:56.838325-04:30	1	17	3	Administrativo	1	
4	2013-09-19 20:10:41.57168-04:30	1	24	1	Venezuela	1	
5	2013-09-19 20:10:42.716314-04:30	1	23	1	Guárico	1	
6	2013-09-19 20:10:44.522547-04:30	1	22	1	Juan Germán Roscio	1	
7	2013-09-19 20:10:46.359969-04:30	1	21	1	San Juan de los Morros	1	
8	2013-09-19 20:11:01.265856-04:30	1	19	1	Principal	1	
9	2013-09-19 20:11:09.143619-04:30	1	19	2	Núcleo	1	
10	2013-09-19 20:12:29.981014-04:30	1	20	1	20	1	
11	2013-09-19 20:13:57.055278-04:30	1	2	1	Rector(a)	1	
12	2013-09-19 20:14:12.863495-04:30	1	18	1	(R) Rectorado	1	
13	2013-09-19 20:14:41.292377-04:30	1	18	2	(R) Rectorado	1	
14	2013-09-19 20:16:01.93075-04:30	1	16	1	Rector(a) de (R) Rectorado	1	
15	2013-09-19 20:26:47.587823-04:30	1	15	1	María Medina	1	
16	2013-09-19 20:35:31.816779-04:30	1	20	2	7	1	
17	2013-09-19 20:36:35.360388-04:30	1	2	2	Decano(a)	1	
18	2013-09-19 20:36:45.384539-04:30	1	18	3	(AIS) Área de Ingeniería en Sistemas	1	
19	2013-09-19 20:37:31.409727-04:30	1	2	3	Coordinador	1	
20	2013-09-19 20:37:33.962996-04:30	1	16	2	Coordinador de (AIS) Área de Ingeniería en Sistemas	1	
21	2013-09-19 20:39:22.793595-04:30	1	15	2	Alberto Rodríguez	1	
22	2013-09-21 15:31:51.86109-04:30	4	20	3	50	1	
23	2013-09-21 15:32:16.895016-04:30	4	2	4	DIrector(a)	1	
24	2013-09-21 15:32:26.267663-04:30	4	18	4	(DACE) Dirección de Admisión, Control y Evaluación	1	
25	2013-09-21 15:32:47.10464-04:30	4	16	3	DIrector(a) de (DACE) Dirección de Admisión, Control y Evaluación	1	
26	2013-09-21 15:34:38.248628-04:30	4	15	3	Edgar Palomares	1	
27	2013-09-21 15:39:32.35281-04:30	4	20	4	30	1	
28	2013-09-21 15:40:46.108897-04:30	4	2	5	Secretaria	1	
29	2013-09-21 15:40:48.892153-04:30	4	18	5	(S) Secretaría	1	
30	2013-09-21 15:42:16.388892-04:30	4	20	5	8	1	
31	2013-09-21 15:42:45.288006-04:30	4	18	6	(DI) Dirección de Informática	1	
32	2013-09-21 15:43:02.965879-04:30	4	16	4	DIrector(a) de (DI) Dirección de Informática	1	
33	2013-09-21 15:45:46.068441-04:30	4	2	6	Programador(a)	1	
34	2013-09-21 15:45:47.739199-04:30	4	16	5	Programador(a) de (DI) Dirección de Informática	1	
35	2013-09-21 15:45:55.543973-04:30	4	15	4	Jennifer Montilla	1	
36	2013-09-21 16:54:58.214187-04:30	4	15	5	Miguel González	1	
37	2013-09-21 17:27:36.752297-04:30	4	15	6	Axel Díaz	1	
38	2013-09-22 11:22:00.903452-04:30	4	2	3	Coordinador(a)	2	Modificado/a name.
39	2013-09-22 11:27:23.996713-04:30	4	18	2	(R) Rectorado	3	
40	2013-09-22 16:24:23.8996-04:30	4	14	1	<Message: 1 destino, 1 con copia>	1	Mensaje enviado exitosamente
41	2013-09-22 16:24:23.947244-04:30	4	14	2	<Message: 1 destino, 1 con copia>	1	Mensaje enviado exitosamente
42	2013-09-23 08:44:38.399254-04:30	4	14	3	<Message: Múltiples destinos>	1	Mensaje enviado exitosamente
43	2013-09-23 08:44:38.494357-04:30	4	14	4	<Message: Múltiples destinos>	1	Mensaje enviado exitosamente
44	2013-09-23 08:44:38.569526-04:30	4	14	5	<Message: Múltiples destinos>	1	Mensaje enviado exitosamente
45	2013-09-23 08:44:38.634085-04:30	4	14	6	<Message: Múltiples destinos>	1	Mensaje enviado exitosamente
46	2013-09-23 09:35:30.732712-04:30	4	14	7	<Message: 1 destino, varias copias>	1	Mensaje enviado exitosamente
47	2013-09-23 09:35:30.785786-04:30	4	14	8	<Message: 1 destino, varias copias>	1	Mensaje enviado exitosamente
48	2013-09-23 09:36:40.08641-04:30	4	14	9	<Message: 2 destinos, sin copia>	1	Mensaje enviado exitosamente
49	2013-09-23 09:36:40.153479-04:30	4	14	10	<Message: 2 destinos, sin copia>	1	Mensaje enviado exitosamente
50	2013-09-23 09:36:40.220445-04:30	4	14	11	<Message: 2 destinos, sin copia>	1	Mensaje enviado exitosamente
51	2013-09-23 10:38:36.708632-04:30	4	14	11	2 destinos, sin copia	2	No ha cambiado ningún campo.
52	2013-09-23 10:39:10.579826-04:30	4	14	12	<Message: Múltiples destinos, múltiples copias>	1	Mensaje enviado exitosamente
53	2013-09-23 10:39:10.670284-04:30	4	14	13	<Message: Múltiples destinos, múltiples copias>	1	Mensaje enviado exitosamente
54	2013-09-23 10:39:10.732514-04:30	4	14	14	<Message: Múltiples destinos, múltiples copias>	1	Mensaje enviado exitosamente
55	2013-09-23 10:40:11.792122-04:30	4	14	1	1 destino, 1 con copia	2	No ha cambiado ningún campo.
56	2013-09-23 10:40:13.67577-04:30	4	14	2	1 destino, 1 con copia	2	No ha cambiado ningún campo.
57	2013-09-23 10:40:15.353798-04:30	4	14	3	Múltiples destinos	2	No ha cambiado ningún campo.
58	2013-09-23 10:40:16.909935-04:30	4	14	4	Múltiples destinos	2	No ha cambiado ningún campo.
59	2013-09-23 10:40:40.180741-04:30	4	14	5	Múltiples destinos	2	No ha cambiado ningún campo.
60	2013-09-23 10:40:43.862027-04:30	4	14	6	Múltiples destinos	2	No ha cambiado ningún campo.
61	2013-09-23 10:40:44.828382-04:30	4	14	7	1 destino, varias copias	2	No ha cambiado ningún campo.
62	2013-09-23 10:40:53.386632-04:30	4	14	8	1 destino, varias copias	2	No ha cambiado ningún campo.
63	2013-09-23 10:40:55.556639-04:30	4	14	9	2 destinos, sin copia	2	No ha cambiado ningún campo.
64	2013-09-23 10:40:57.687393-04:30	4	14	10	2 destinos, sin copia	2	No ha cambiado ningún campo.
65	2013-09-23 14:39:10.614711-04:30	4	3	1	f0ry	2	Modificado/a username, password y email.
66	2013-10-02 17:52:20.681965-04:30	1	14	10	2 destinos, sin copia	2	Modificado/a sender.
67	2013-10-02 17:52:49.622266-04:30	1	14	9	2 destinos, sin copia	2	Modificado/a sender.
68	2013-10-02 17:53:05.493676-04:30	1	14	8	1 destino, varias copias	2	Modificado/a sender.
69	2013-10-02 17:53:33.384403-04:30	1	14	7	1 destino, varias copias	2	Modificado/a sender.
70	2013-10-02 17:55:34.505858-04:30	1	14	7	1 destino, varias copias	2	Modificado/a recipient.
71	2013-10-02 17:55:44.652158-04:30	1	14	7	1 destino, varias copias	2	No ha cambiado ningún campo.
72	2013-10-02 17:55:50.952045-04:30	1	14	7	1 destino, varias copias	2	No ha cambiado ningún campo.
73	2013-10-02 17:56:02.76708-04:30	1	14	8	1 destino, varias copias	2	Modificado/a recipient.
74	2013-10-02 17:56:20.356156-04:30	1	14	9	2 destinos, sin copia	2	Modificado/a recipient y sender.
75	2013-10-02 17:56:35.974378-04:30	1	14	8	1 destino, varias copias	2	Modificado/a sender.
76	2013-10-02 17:56:51.257845-04:30	1	14	7	1 destino, varias copias	2	Modificado/a sender.
77	2013-10-02 17:58:20.589605-04:30	1	14	7	1 destino, varias copias	2	Modificado/a status.
78	2013-10-02 17:58:40.901301-04:30	1	14	8	1 destino, varias copias	2	Modificado/a status.
79	2013-10-02 17:58:57.315437-04:30	1	14	9	2 destinos, sin copia	2	Modificado/a status.
80	2013-10-02 18:00:41.508523-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
81	2013-10-02 18:01:21.235275-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
82	2013-10-02 18:01:42.365215-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
83	2013-10-02 18:03:12.853616-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
84	2013-10-02 18:03:39.019193-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
85	2013-10-02 18:03:51.496039-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
86	2013-10-02 18:20:17.2893-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
87	2013-10-02 18:20:38.933204-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
88	2013-10-02 18:21:02.287302-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
89	2013-10-02 18:21:14.732355-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
90	2013-10-02 18:22:52.593077-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
91	2013-10-02 18:23:09.893673-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
92	2013-10-02 18:23:54.369208-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
93	2013-10-02 18:24:31.02138-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
94	2013-10-02 18:40:49.058649-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
95	2013-10-02 18:45:24.576752-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
96	2013-10-02 18:45:36.50987-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
97	2013-10-02 18:50:19.507653-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
98	2013-10-02 18:51:17.171367-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
99	2013-10-02 18:53:16.477063-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
100	2013-10-02 20:10:54.709347-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
101	2013-10-02 20:14:26.485036-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
102	2013-10-02 20:14:48.607886-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
103	2013-10-02 20:16:25.846721-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
104	2013-10-02 20:16:44.390775-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
105	2013-10-02 20:18:13.67414-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
106	2013-10-02 20:19:04.058845-04:30	1	14	7	<Message: 1 destino, varias copias>	2	Mensaje nuevo leído.
107	2013-10-02 20:57:38.712199-04:30	4	14	15	<Message: >	1	Mensaje enviado exitosamente
108	2013-10-02 21:06:09.934482-04:30	4	14	16	<Message: >	1	Mensaje enviado exitosamente
109	2013-10-02 21:10:11.529007-04:30	4	14	16		3	
110	2013-10-02 21:10:11.569849-04:30	4	14	15		3	
111	2013-10-02 21:11:27.23583-04:30	4	14	17	<Message: >	1	Mensaje enviado exitosamente
112	2013-10-02 21:12:13.906774-04:30	4	14	17		3	
113	2013-10-02 21:12:23.80173-04:30	4	14	18	<Message: >	1	Mensaje enviado exitosamente
114	2013-10-02 21:12:50.556687-04:30	4	14	18		3	
115	2013-10-02 21:16:24.244792-04:30	4	14	19	<Message: >	1	Mensaje enviado exitosamente
116	2013-10-02 22:56:01.526064-04:30	4	14	27		3	
117	2013-10-02 22:56:01.663682-04:30	4	14	26		3	
118	2013-10-02 22:56:01.684376-04:30	4	14	25		3	
119	2013-10-02 22:56:01.708775-04:30	4	14	24		3	
120	2013-10-02 22:56:01.729167-04:30	4	14	23		3	
121	2013-10-02 22:56:01.751513-04:30	4	14	22		3	
122	2013-10-02 22:56:01.773687-04:30	4	14	21		3	
123	2013-10-02 22:56:01.795815-04:30	4	14	20		3	
124	2013-10-02 22:56:01.818884-04:30	4	14	19		3	
125	2013-10-02 23:02:17.238923-04:30	4	14	28		3	
126	2013-10-04 13:12:49.306998-04:30	4	14	35		3	
127	2013-10-04 13:12:49.427694-04:30	4	14	34		3	
128	2013-10-04 13:12:49.452687-04:30	4	14	33		3	
129	2013-10-04 13:12:49.471346-04:30	4	14	30		3	
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 129, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	pregunta	auth	pregunta
5	Pregunta secreta	auth	preguntassecretas
6	Usuario	auth	userprofile
7	log entry	admin	logentry
8	content type	contenttypes	contenttype
9	session	sessions	session
10	site	sites	site
11	destinatario	django_messages	destinatarios
12	estado memo	django_messages	estadomemo
13	adjunto	django_messages	adjunto
14	Message	django_messages	message
15	personas	personas	personas
16	personal	personas	personal
17	tipo de personal	personas	tipopersonal
18	dependencia	sedes	dependencias
19	tipo de sede	sedes	tiposede
20	nivel	sedes	niveles
21	parroquia	sedes	parroquias
22	municipio	sedes	municipio
23	estado	sedes	estado
24	país	sedes	pais
25	noticias	noticias	noticias
26	comentarios	reportes	comentarios
27	manual_ detalles	manual_usuario	manual_detalles
28	manual	manual_usuario	manual
29	key map	django_select2	keymap
30	Folder	filer	folder
31	folder permission	filer	folderpermission
32	file	filer	file
33	clipboard	filer	clipboard
34	clipboard item	filer	clipboarditem
35	image	filer	image
36	respuestas	reportes	respuestas
37	migration history	south	migrationhistory
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_content_type_id_seq', 37, true);


--
-- Data for Name: django_messages_estadomemo; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_messages_estadomemo (id, nombre) FROM stdin;
1	Aprobado
3	En espera
4	Anulado
\.


--
-- Name: django_messages_estadomemo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_messages_estadomemo_id_seq', 4, true);


--
-- Data for Name: django_messages_estadomemo_modificable; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_messages_estadomemo_modificable (id, estadomemo_id, group_id) FROM stdin;
1	1	1
2	3	3
3	4	2
\.


--
-- Name: django_messages_estadomemo_modificable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_messages_estadomemo_modificable_id_seq', 3, true);


--
-- Data for Name: django_messages_message; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_messages_message (id, recipient_id, con_copia, subject, archivo, body, sender_id, parent_msg_id, sent_at, read_at, replied_at, deleted_at, status_id, tipo, codigo, num_ident, borrador) FROM stdin;
11	11	t	2 destinos, sin copia		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:38:36.568747-04:30	\N	\N	\N	3		56494934770	1	f
12	12	f	Múltiples destinos, múltiples copias		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:39:10.48814-04:30	\N	\N	\N	3		49494949479095	2	f
13	7	f	Múltiples destinos, múltiples copias		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:39:10.637457-04:30	\N	\N	\N	3		49494949479095	2	f
14	11	t	Múltiples destinos, múltiples copias		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:39:10.703763-04:30	\N	\N	\N	3		49494949479095	2	f
1	5	f	1 destino, 1 con copia		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:11.769923-04:30	\N	\N	\N	3		484949708234	1	f
2	11	t	1 destino, 1 con copia		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:13.635999-04:30	\N	\N	\N	3		484949708234	1	f
3	5	f	Múltiples destinos		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:15.324331-04:30	\N	\N	\N	3		504949703990	1	f
4	7	f	Múltiples destinos		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:16.827099-04:30	\N	\N	\N	3		504949703990	1	f
5	10	f	Múltiples destinos		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:40.155732-04:30	\N	\N	\N	3		504949703990	1	f
6	11	f	Múltiples destinos		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-09-23 10:40:43.844023-04:30	\N	\N	\N	3		504949703990	1	f
10	7	f	2 destinos, sin copia		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	10	\N	2013-10-02 17:52:20.649806-04:30	\N	\N	\N	3		56494934770	1	f
8	10	t	1 destino, varias copias		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	2	\N	2013-10-02 17:58:40.869413-04:30	\N	\N	\N	1		544949409864	1	f
9	10	f	2 destinos, sin copia		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	5	\N	2013-10-02 17:58:57.257739-04:30	\N	\N	\N	1		56494934770	1	f
7	10	f	1 destino, varias copias		\r\n\r\nCordialmente, \r\nAxel Díaz. Programador(a) de (DI) Dirección de Informática	7	\N	2013-10-02 20:19:03.976463-04:30	2013-10-02 20:19:03.753857-04:30	\N	\N	1		544949409864	1	f
41	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-04 17:33:04.320332-04:30	\N	\N	\N	3		49524949315284	2	t
42	\N	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-04 17:33:04.994663-04:30	\N	\N	\N	3		49524949315284	2	t
53	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 16:14:27.002431-04:30	\N	\N	\N	3		49554949415501	5	t
48	7	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-04 20:23:20.723384-04:30	\N	\N	\N	3		49544949981515	4	t
51	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 14:27:48.274334-04:30	\N	\N	\N	3		49554949415501	5	t
52	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 14:42:51.242172-04:30	\N	\N	\N	3		49554949415501	5	t
67	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:25:18.875124-04:30	\N	\N	\N	3		51484949628389	18	t
68	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:27:14.834201-04:30	\N	\N	\N	3		51484949628389	18	t
54	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 16:20:43.375991-04:30	\N	\N	\N	3		49554949415501	5	t
55	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:05:30.354265-04:30	\N	\N	\N	3		50494949347381	9	t
56	\N	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:05:30.643044-04:30	\N	\N	\N	3		50494949347381	9	t
57	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:08:14.197889-04:30	\N	\N	\N	3		50514949193301	11	t
58	\N	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:09:05.426942-04:30	\N	\N	\N	3		50514949193301	11	t
59	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:09:27.277397-04:30	\N	\N	\N	3		50534949268625	13	t
60	\N	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:09:38.958024-04:30	\N	\N	\N	3		50534949268625	13	t
61	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:11:21.531049-04:30	\N	\N	\N	3		50554949523818	15	t
62	\N	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:13:49.606609-04:30	\N	\N	\N	3		50554949523818	15	t
63	\N	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:14:46.865571-04:30	\N	\N	\N	3		50574949853099	17	t
65	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:21:05.967276-04:30	\N	\N	\N	3		51484949628389	18	t
66	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:23:20.577698-04:30	\N	\N	\N	3		51484949628389	18	t
69	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:29:12.411701-04:30	\N	\N	\N	3		51484949628389	18	t
70	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:37:30.815721-04:30	\N	\N	\N	3		51484949628389	18	t
71	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:39:29.599729-04:30	\N	\N	\N	3		51484949628389	18	t
72	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 17:45:36.251639-04:30	\N	\N	\N	3		51484949628389	18	t
73	12	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 19:04:49.694226-04:30	\N	\N	\N	3		51484949628389	18	t
74	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 21:30:52.130849-04:30	\N	\N	\N	3		51574949123646	27	t
75	5	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 21:30:52.350625-04:30	\N	\N	\N	3		51574949123646	27	t
76	12	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 21:30:52.384746-04:30	\N	\N	\N	3		51574949123646	27	t
77	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 22:58:53.453635-04:30	\N	\N	\N	3		52504949420703	30	t
78	5	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 22:58:54.235848-04:30	\N	\N	\N	3		52504949420703	30	t
79	12	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 22:58:54.289282-04:30	\N	\N	\N	3		52504949420703	30	t
80	5	f			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 23:03:28.123435-04:30	\N	\N	\N	3		52534949112263	33	t
81	5	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 23:03:28.35158-04:30	\N	\N	\N	3		52534949112263	33	t
82	12	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-14 23:03:39.3702-04:30	\N	\N	\N	3		52534949112263	33	t
83	5	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-15 00:08:01.297444-04:30	\N	\N	\N	3		52564949285654	36	t
84	12	t			Cordialmente, Axel Díaz. Programador(a) de (DI) Dirección de Informática	12	\N	2013-10-15 00:08:01.513797-04:30	\N	\N	\N	3		52564949285654	36	t
\.


--
-- Name: django_messages_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_messages_message_id_seq', 84, true);


--
-- Data for Name: django_select2_keymap; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_select2_keymap (id, key, value, accessed_on) FROM stdin;
\.


--
-- Name: django_select2_keymap_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_select2_keymap_id_seq', 1, false);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
98pojqnogrt4gl1lv0stubghvcjje5bf	ODU4YmQyMzViYjA1YWI3MTg2Nzg5MDliMTI1MGRlZWEyOGE5NzExYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-10-03 19:58:32.708701-04:30
zmky8huw0bsrinfcxc96mj17glaq5s8j	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-04 11:13:21.876574-04:30
ctc22xge5zhkvbpmfhgezi3shpz3pfwz	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-05 15:24:43.301377-04:30
ymu1n0ot0vid5hloaxgiv5d88lby3xjv	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-06 11:08:03.960694-04:30
yd6ps3sumwtnt3st6az36alvj6j5gcu5	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-06 11:15:46.694631-04:30
3qwi67am87d13hlvqd5gxqfrxtfimu8v	ODhlYWM5NzIzMDI2Mzc0YTFmZjIzN2IzMTU0NjJiOGRhMzZmZDkyZjqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu	2013-10-06 16:15:25.188996-04:30
b5cancq3hjc4iv25bd7c9qt85vwv9y4y	ODhlYWM5NzIzMDI2Mzc0YTFmZjIzN2IzMTU0NjJiOGRhMzZmZDkyZjqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu	2013-10-06 16:15:25.44839-04:30
65twglgzcrzsnoxkx0ukjmo3c4vo2606	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-06 16:15:29.731848-04:30
2jgidrw7dds2d4raxemjsyb4bpocfa4e	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-07 06:58:17.172265-04:30
d68pc454ebesocuxgezxpnxobl7ffkw2	ZTQ0MGEzODFjYWI3MWQ0ZmE0YTE3M2Y3YTQwZmE3MTI5ZDFiNDc2ZDqAAn1xAS4=	2013-10-07 14:11:41.98918-04:30
wqiev600rwfs6m61odj6ukxfpi0dta4g	ODU4YmQyMzViYjA1YWI3MTg2Nzg5MDliMTI1MGRlZWEyOGE5NzExYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-10-07 15:07:38.928297-04:30
3cwfd18gmexceeh78iuop5zbwwn1ljxa	ODU4YmQyMzViYjA1YWI3MTg2Nzg5MDliMTI1MGRlZWEyOGE5NzExYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-10-09 14:25:09.979891-04:30
tnb3f1ez2c2opvlr80zosecdkgk9agfq	ODU4YmQyMzViYjA1YWI3MTg2Nzg5MDliMTI1MGRlZWEyOGE5NzExYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-10-16 17:51:08.302161-04:30
ak75ikki8c53hmm74tdbb4eyiyr8yod1	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-16 17:55:54.059941-04:30
nk9eezgy2u5shr440d6rmmgbwvfc09cx	NmYwMzliMzEwMmZkOGQ5Y2NiN2ViMmUxMGU4ODllOWUxM2VmMTg2NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu	2013-10-21 01:23:54.898738-04:30
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: estado; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY estado (id, nombre, pais_id) FROM stdin;
1	Guárico	1
\.


--
-- Name: estado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('estado_id_seq', 1, true);


--
-- Data for Name: filer_clipboard; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_clipboard (id, user_id) FROM stdin;
\.


--
-- Name: filer_clipboard_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('filer_clipboard_id_seq', 1, false);


--
-- Data for Name: filer_clipboarditem; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_clipboarditem (id, file_id, clipboard_id) FROM stdin;
\.


--
-- Name: filer_clipboarditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('filer_clipboarditem_id_seq', 1, false);


--
-- Data for Name: filer_file; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_file (id, polymorphic_ctype_id, folder_id, file, _file_size, sha1, has_all_mandatory_data, original_filename, name, description, owner_id, uploaded_at, modified_at, is_public) FROM stdin;
\.


--
-- Name: filer_file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('filer_file_id_seq', 1, false);


--
-- Data for Name: filer_folder; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_folder (id, parent_id, name, owner_id, uploaded_at, created_at, modified_at, lft, rght, tree_id, level) FROM stdin;
\.


--
-- Name: filer_folder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('filer_folder_id_seq', 1, false);


--
-- Data for Name: filer_folderpermission; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_folderpermission (id, folder_id, type, user_id, group_id, everybody, can_edit, can_read, can_add_children) FROM stdin;
\.


--
-- Name: filer_folderpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('filer_folderpermission_id_seq', 1, false);


--
-- Data for Name: filer_image; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY filer_image (file_ptr_id, _height, _width, date_taken, default_alt_text, default_caption, author, must_always_publish_author_credit, must_always_publish_copyright, subject_location) FROM stdin;
\.


--
-- Data for Name: manual_usuario; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY manual_usuario (id, titulo, seccion) FROM stdin;
\.


--
-- Data for Name: manual_usuario_detalles; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY manual_usuario_detalles (id, manual_id, texto, imagen) FROM stdin;
\.


--
-- Name: manual_usuario_detalles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('manual_usuario_detalles_id_seq', 1, false);


--
-- Name: manual_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('manual_usuario_id_seq', 1, false);


--
-- Data for Name: municipio; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY municipio (id, nombre, estado_id) FROM stdin;
1	Juan Germán Roscio	1
\.


--
-- Name: municipio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('municipio_id_seq', 1, true);


--
-- Data for Name: niveles; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY niveles (id, numero) FROM stdin;
1	20
2	7
3	50
4	30
5	8
\.


--
-- Name: niveles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('niveles_id_seq', 5, true);


--
-- Data for Name: noticias; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY noticias (id, titulo, texto, fecha) FROM stdin;
\.


--
-- Name: noticias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('noticias_id_seq', 1, false);


--
-- Data for Name: pais; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY pais (id, nombre) FROM stdin;
1	Venezuela
\.


--
-- Name: pais_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('pais_id_seq', 1, true);


--
-- Data for Name: parroquia; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY parroquia (id, nombre, municipio_id) FROM stdin;
1	San Juan de los Morros	1
\.


--
-- Name: parroquia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('parroquia_id_seq', 1, true);


--
-- Data for Name: personal; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY personal (id, tipo_personal_id, dependencia_id, cargo_id) FROM stdin;
1	3	1	1
2	1	3	3
3	3	4	4
4	3	6	4
5	3	6	6
\.


--
-- Name: personal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('personal_id_seq', 5, true);


--
-- Data for Name: personas; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY personas (id, tipodoc, num_identificacion, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, genero, email, telefono, cargo_principal_id) FROM stdin;
1	c	8631858	Medina		María	Arisela	1	mariadepalm@udefa.edu.ve	02464316721	1
2	c	16407820	Rodríguez		Alberto		0	arod.unerg@gmail.com	04127609320	2
3	c	 16552619	Palomares		Edgar		0	edgaropalomaresm@gmail.com		3
4	c	19725648	Montilla		Jennifer		0	a@b.com		5
5	c	15498350	González	Carmona	Miguel	Ramón	0	mrgc71@gmail.com		4
6	c	19276008	Díaz		Axel		0	correo@correo.com		5
\.


--
-- Data for Name: personas_cargos_autorizados; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY personas_cargos_autorizados (id, personas_id, personal_id) FROM stdin;
\.


--
-- Name: personas_cargos_autorizados_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('personas_cargos_autorizados_id_seq', 1, false);


--
-- Name: personas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('personas_id_seq', 6, true);


--
-- Data for Name: respuestas; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY respuestas (id, pregunta_id, comentario, usuario_id, respondido) FROM stdin;
\.


--
-- Name: respuestas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('respuestas_id_seq', 1, false);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	django_messages	0001_initial	2013-10-02 19:16:04.32354-04:30
2	django_messages	0002_auto__add_field_message_borrador	2013-10-02 19:21:33.016326-04:30
3	django_messages	0003_auto__chg_field_message_body__chg_field_message_subject__chg_field_mes	2013-10-02 20:16:53.592716-04:30
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 3, true);


--
-- Data for Name: tipo_personal; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY tipo_personal (id, nombre) FROM stdin;
1	Académico
2	Obrero
3	Administrativo
\.


--
-- Name: tipo_personal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('tipo_personal_id_seq', 3, true);


--
-- Data for Name: tipo_sede; Type: TABLE DATA; Schema: public; Owner: umail
--

COPY tipo_sede (id, nombre) FROM stdin;
1	Principal
2	Núcleo
\.


--
-- Name: tipo_sede_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umail
--

SELECT pg_catalog.setval('tipo_sede_id_seq', 2, true);


--
-- Name: adjuntos_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY adjuntos
    ADD CONSTRAINT adjuntos_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_pregunta_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_pregunta
    ADD CONSTRAINT auth_pregunta_pkey PRIMARY KEY (id);


--
-- Name: auth_preguntassecretas_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_preguntassecretas
    ADD CONSTRAINT auth_preguntassecretas_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: auth_userprofile_persona_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_userprofile
    ADD CONSTRAINT auth_userprofile_persona_id_key UNIQUE (persona_id);


--
-- Name: auth_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_userprofile
    ADD CONSTRAINT auth_userprofile_pkey PRIMARY KEY (id);


--
-- Name: auth_userprofile_user_id_persona_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY auth_userprofile
    ADD CONSTRAINT auth_userprofile_user_id_persona_id_key UNIQUE (user_id, persona_id);


--
-- Name: comentarios_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY comentarios
    ADD CONSTRAINT comentarios_pkey PRIMARY KEY (id);


--
-- Name: dependencias_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT dependencias_pkey PRIMARY KEY (id);


--
-- Name: dependencias_telefono_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT dependencias_telefono_key UNIQUE (telefono);


--
-- Name: destinatarios_grupos_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY destinatarios
    ADD CONSTRAINT destinatarios_grupos_id_key UNIQUE (grupos_id);


--
-- Name: destinatarios_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY destinatarios
    ADD CONSTRAINT destinatarios_pkey PRIMARY KEY (id);


--
-- Name: destinatarios_usuarios_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY destinatarios
    ADD CONSTRAINT destinatarios_usuarios_id_key UNIQUE (usuarios_id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_messages_estadomemo_modificab_estadomemo_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_messages_estadomemo_modificable
    ADD CONSTRAINT django_messages_estadomemo_modificab_estadomemo_id_group_id_key UNIQUE (estadomemo_id, group_id);


--
-- Name: django_messages_estadomemo_modificable_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_messages_estadomemo_modificable
    ADD CONSTRAINT django_messages_estadomemo_modificable_pkey PRIMARY KEY (id);


--
-- Name: django_messages_estadomemo_nombre_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_messages_estadomemo
    ADD CONSTRAINT django_messages_estadomemo_nombre_key UNIQUE (nombre);


--
-- Name: django_messages_estadomemo_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_messages_estadomemo
    ADD CONSTRAINT django_messages_estadomemo_pkey PRIMARY KEY (id);


--
-- Name: django_messages_message_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_messages_message
    ADD CONSTRAINT django_messages_message_pkey PRIMARY KEY (id);


--
-- Name: django_select2_keymap_key_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_select2_keymap
    ADD CONSTRAINT django_select2_keymap_key_key UNIQUE (key);


--
-- Name: django_select2_keymap_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_select2_keymap
    ADD CONSTRAINT django_select2_keymap_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: estado_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id);


--
-- Name: filer_clipboard_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_clipboard
    ADD CONSTRAINT filer_clipboard_pkey PRIMARY KEY (id);


--
-- Name: filer_clipboarditem_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_clipboarditem
    ADD CONSTRAINT filer_clipboarditem_pkey PRIMARY KEY (id);


--
-- Name: filer_file_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_file
    ADD CONSTRAINT filer_file_pkey PRIMARY KEY (id);


--
-- Name: filer_folder_parent_id_name_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_folder
    ADD CONSTRAINT filer_folder_parent_id_name_key UNIQUE (parent_id, name);


--
-- Name: filer_folder_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_folder
    ADD CONSTRAINT filer_folder_pkey PRIMARY KEY (id);


--
-- Name: filer_folderpermission_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_folderpermission
    ADD CONSTRAINT filer_folderpermission_pkey PRIMARY KEY (id);


--
-- Name: filer_image_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY filer_image
    ADD CONSTRAINT filer_image_pkey PRIMARY KEY (file_ptr_id);


--
-- Name: manual_usuario_detalles_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY manual_usuario_detalles
    ADD CONSTRAINT manual_usuario_detalles_pkey PRIMARY KEY (id);


--
-- Name: manual_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY manual_usuario
    ADD CONSTRAINT manual_usuario_pkey PRIMARY KEY (id);


--
-- Name: municipio_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY municipio
    ADD CONSTRAINT municipio_pkey PRIMARY KEY (id);


--
-- Name: niveles_numero_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY niveles
    ADD CONSTRAINT niveles_numero_key UNIQUE (numero);


--
-- Name: niveles_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY niveles
    ADD CONSTRAINT niveles_pkey PRIMARY KEY (id);


--
-- Name: noticias_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY noticias
    ADD CONSTRAINT noticias_pkey PRIMARY KEY (id);


--
-- Name: pais_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY pais
    ADD CONSTRAINT pais_pkey PRIMARY KEY (id);


--
-- Name: parroquia_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY parroquia
    ADD CONSTRAINT parroquia_pkey PRIMARY KEY (id);


--
-- Name: personal_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY personal
    ADD CONSTRAINT personal_pkey PRIMARY KEY (id);


--
-- Name: personas_cargos_autorizados_personas_id_personal_id_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY personas_cargos_autorizados
    ADD CONSTRAINT personas_cargos_autorizados_personas_id_personal_id_key UNIQUE (personas_id, personal_id);


--
-- Name: personas_cargos_autorizados_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY personas_cargos_autorizados
    ADD CONSTRAINT personas_cargos_autorizados_pkey PRIMARY KEY (id);


--
-- Name: personas_num_identificacion_key; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY personas
    ADD CONSTRAINT personas_num_identificacion_key UNIQUE (num_identificacion);


--
-- Name: personas_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY personas
    ADD CONSTRAINT personas_pkey PRIMARY KEY (id);


--
-- Name: respuestas_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY respuestas
    ADD CONSTRAINT respuestas_pkey PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: tipo_personal_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY tipo_personal
    ADD CONSTRAINT tipo_personal_pkey PRIMARY KEY (id);


--
-- Name: tipo_sede_pkey; Type: CONSTRAINT; Schema: public; Owner: umail; Tablespace: 
--

ALTER TABLE ONLY tipo_sede
    ADD CONSTRAINT tipo_sede_pkey PRIMARY KEY (id);


--
-- Name: adjuntos_mensaje_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX adjuntos_mensaje_id ON adjuntos USING btree (mensaje_id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_preguntassecretas_pregunta_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_preguntassecretas_pregunta_id ON auth_preguntassecretas USING btree (pregunta_id);


--
-- Name: auth_preguntassecretas_usuario_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_preguntassecretas_usuario_id ON auth_preguntassecretas USING btree (usuario_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_userprofile_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX auth_userprofile_user_id ON auth_userprofile USING btree (user_id);


--
-- Name: dependencias_cargo_max_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX dependencias_cargo_max_id ON dependencias USING btree (cargo_max_id);


--
-- Name: dependencias_dependencia_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX dependencias_dependencia_id ON dependencias USING btree (dependencia_id);


--
-- Name: dependencias_nivel_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX dependencias_nivel_id ON dependencias USING btree (nivel_id);


--
-- Name: dependencias_tipo_sede_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX dependencias_tipo_sede_id ON dependencias USING btree (tipo_sede_id);


--
-- Name: dependencias_ubicacion_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX dependencias_ubicacion_id ON dependencias USING btree (ubicacion_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_messages_estadomemo_modificable_estadomemo_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_estadomemo_modificable_estadomemo_id ON django_messages_estadomemo_modificable USING btree (estadomemo_id);


--
-- Name: django_messages_estadomemo_modificable_group_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_estadomemo_modificable_group_id ON django_messages_estadomemo_modificable USING btree (group_id);


--
-- Name: django_messages_estadomemo_nombre_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_estadomemo_nombre_like ON django_messages_estadomemo USING btree (nombre varchar_pattern_ops);


--
-- Name: django_messages_message_parent_msg_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_message_parent_msg_id ON django_messages_message USING btree (parent_msg_id);


--
-- Name: django_messages_message_recipient_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_message_recipient_id ON django_messages_message USING btree (recipient_id);


--
-- Name: django_messages_message_sender_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_message_sender_id ON django_messages_message USING btree (sender_id);


--
-- Name: django_messages_message_status_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_messages_message_status_id ON django_messages_message USING btree (status_id);


--
-- Name: django_select2_keymap_key_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_select2_keymap_key_like ON django_select2_keymap USING btree (key varchar_pattern_ops);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: estado_pais_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX estado_pais_id ON estado USING btree (pais_id);


--
-- Name: filer_clipboard_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_clipboard_user_id ON filer_clipboard USING btree (user_id);


--
-- Name: filer_clipboarditem_clipboard_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_clipboarditem_clipboard_id ON filer_clipboarditem USING btree (clipboard_id);


--
-- Name: filer_clipboarditem_file_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_clipboarditem_file_id ON filer_clipboarditem USING btree (file_id);


--
-- Name: filer_file_folder_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_file_folder_id ON filer_file USING btree (folder_id);


--
-- Name: filer_file_owner_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_file_owner_id ON filer_file USING btree (owner_id);


--
-- Name: filer_file_polymorphic_ctype_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_file_polymorphic_ctype_id ON filer_file USING btree (polymorphic_ctype_id);


--
-- Name: filer_folder_level; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_level ON filer_folder USING btree (level);


--
-- Name: filer_folder_lft; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_lft ON filer_folder USING btree (lft);


--
-- Name: filer_folder_owner_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_owner_id ON filer_folder USING btree (owner_id);


--
-- Name: filer_folder_parent_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_parent_id ON filer_folder USING btree (parent_id);


--
-- Name: filer_folder_rght; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_rght ON filer_folder USING btree (rght);


--
-- Name: filer_folder_tree_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folder_tree_id ON filer_folder USING btree (tree_id);


--
-- Name: filer_folderpermission_folder_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folderpermission_folder_id ON filer_folderpermission USING btree (folder_id);


--
-- Name: filer_folderpermission_group_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folderpermission_group_id ON filer_folderpermission USING btree (group_id);


--
-- Name: filer_folderpermission_user_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX filer_folderpermission_user_id ON filer_folderpermission USING btree (user_id);


--
-- Name: manual_usuario_detalles_manual_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX manual_usuario_detalles_manual_id ON manual_usuario_detalles USING btree (manual_id);


--
-- Name: municipio_estado_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX municipio_estado_id ON municipio USING btree (estado_id);


--
-- Name: parroquia_municipio_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX parroquia_municipio_id ON parroquia USING btree (municipio_id);


--
-- Name: personal_cargo_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personal_cargo_id ON personal USING btree (cargo_id);


--
-- Name: personal_dependencia_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personal_dependencia_id ON personal USING btree (dependencia_id);


--
-- Name: personal_tipo_personal_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personal_tipo_personal_id ON personal USING btree (tipo_personal_id);


--
-- Name: personas_cargo_principal_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personas_cargo_principal_id ON personas USING btree (cargo_principal_id);


--
-- Name: personas_cargos_autorizados_personal_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personas_cargos_autorizados_personal_id ON personas_cargos_autorizados USING btree (personal_id);


--
-- Name: personas_cargos_autorizados_personas_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personas_cargos_autorizados_personas_id ON personas_cargos_autorizados USING btree (personas_id);


--
-- Name: personas_num_identificacion_like; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX personas_num_identificacion_like ON personas USING btree (num_identificacion varchar_pattern_ops);


--
-- Name: respuestas_pregunta_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX respuestas_pregunta_id ON respuestas USING btree (pregunta_id);


--
-- Name: respuestas_usuario_id; Type: INDEX; Schema: public; Owner: umail; Tablespace: 
--

CREATE INDEX respuestas_usuario_id ON respuestas USING btree (usuario_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_preguntassecretas_pregunta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_preguntassecretas
    ADD CONSTRAINT auth_preguntassecretas_pregunta_id_fkey FOREIGN KEY (pregunta_id) REFERENCES auth_pregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_preguntassecretas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_preguntassecretas
    ADD CONSTRAINT auth_preguntassecretas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_userprofile_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_userprofile
    ADD CONSTRAINT auth_userprofile_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cargo_principal_id_refs_id_8100d133; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personas
    ADD CONSTRAINT cargo_principal_id_refs_id_8100d133 FOREIGN KEY (cargo_principal_id) REFERENCES personal(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_93d2d1f8; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dependencia_id_refs_id_7a840b8a; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personal
    ADD CONSTRAINT dependencia_id_refs_id_7a840b8a FOREIGN KEY (dependencia_id) REFERENCES dependencias(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dependencia_id_refs_id_c39529f8; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT dependencia_id_refs_id_c39529f8 FOREIGN KEY (dependencia_id) REFERENCES dependencias(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dependencias_cargo_max_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT dependencias_cargo_max_id_fkey FOREIGN KEY (cargo_max_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: destinatarios_grupos_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY destinatarios
    ADD CONSTRAINT destinatarios_grupos_id_fkey FOREIGN KEY (grupos_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: destinatarios_usuarios_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY destinatarios
    ADD CONSTRAINT destinatarios_usuarios_id_fkey FOREIGN KEY (usuarios_id) REFERENCES auth_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_messages_estadomemo_modificable_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_estadomemo_modificable
    ADD CONSTRAINT django_messages_estadomemo_modificable_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_messages_message_sender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_message
    ADD CONSTRAINT django_messages_message_sender_id_fkey FOREIGN KEY (sender_id) REFERENCES destinatarios(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_messages_message_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_message
    ADD CONSTRAINT django_messages_message_status_id_fkey FOREIGN KEY (status_id) REFERENCES django_messages_estadomemo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: estado_id_refs_id_394e7f1e; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY municipio
    ADD CONSTRAINT estado_id_refs_id_394e7f1e FOREIGN KEY (estado_id) REFERENCES estado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: estadomemo_id_refs_id_bb6bd812; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_estadomemo_modificable
    ADD CONSTRAINT estadomemo_id_refs_id_bb6bd812 FOREIGN KEY (estadomemo_id) REFERENCES django_messages_estadomemo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_clipboard_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_clipboard
    ADD CONSTRAINT filer_clipboard_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_clipboarditem_clipboard_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_clipboarditem
    ADD CONSTRAINT filer_clipboarditem_clipboard_id_fkey FOREIGN KEY (clipboard_id) REFERENCES filer_clipboard(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_clipboarditem_file_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_clipboarditem
    ADD CONSTRAINT filer_clipboarditem_file_id_fkey FOREIGN KEY (file_id) REFERENCES filer_file(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_file_folder_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_file
    ADD CONSTRAINT filer_file_folder_id_fkey FOREIGN KEY (folder_id) REFERENCES filer_folder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_file_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_file
    ADD CONSTRAINT filer_file_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_file_polymorphic_ctype_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_file
    ADD CONSTRAINT filer_file_polymorphic_ctype_id_fkey FOREIGN KEY (polymorphic_ctype_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_folder_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folder
    ADD CONSTRAINT filer_folder_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_folderpermission_folder_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folderpermission
    ADD CONSTRAINT filer_folderpermission_folder_id_fkey FOREIGN KEY (folder_id) REFERENCES filer_folder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_folderpermission_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folderpermission
    ADD CONSTRAINT filer_folderpermission_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_folderpermission_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folderpermission
    ADD CONSTRAINT filer_folderpermission_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: filer_image_file_ptr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_image
    ADD CONSTRAINT filer_image_file_ptr_id_fkey FOREIGN KEY (file_ptr_id) REFERENCES filer_file(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: manual_id_refs_id_e660be64; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY manual_usuario_detalles
    ADD CONSTRAINT manual_id_refs_id_e660be64 FOREIGN KEY (manual_id) REFERENCES manual_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mensaje_id_refs_id_ee95b764; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY adjuntos
    ADD CONSTRAINT mensaje_id_refs_id_ee95b764 FOREIGN KEY (mensaje_id) REFERENCES django_messages_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: municipio_id_refs_id_af1189c5; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY parroquia
    ADD CONSTRAINT municipio_id_refs_id_af1189c5 FOREIGN KEY (municipio_id) REFERENCES municipio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: nivel_id_refs_id_83218ecd; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT nivel_id_refs_id_83218ecd FOREIGN KEY (nivel_id) REFERENCES niveles(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pais_id_refs_id_6c29dca0; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY estado
    ADD CONSTRAINT pais_id_refs_id_6c29dca0 FOREIGN KEY (pais_id) REFERENCES pais(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: parent_id_refs_id_42b2c54f; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY filer_folder
    ADD CONSTRAINT parent_id_refs_id_42b2c54f FOREIGN KEY (parent_id) REFERENCES filer_folder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: parent_msg_id_refs_id_03aad111; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_message
    ADD CONSTRAINT parent_msg_id_refs_id_03aad111 FOREIGN KEY (parent_msg_id) REFERENCES django_messages_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: persona_id_refs_id_662ffbeb; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_userprofile
    ADD CONSTRAINT persona_id_refs_id_662ffbeb FOREIGN KEY (persona_id) REFERENCES personas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: personal_cargo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personal
    ADD CONSTRAINT personal_cargo_id_fkey FOREIGN KEY (cargo_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: personal_id_refs_id_a7cd784c; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personas_cargos_autorizados
    ADD CONSTRAINT personal_id_refs_id_a7cd784c FOREIGN KEY (personal_id) REFERENCES personal(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: personas_id_refs_id_07047a89; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personas_cargos_autorizados
    ADD CONSTRAINT personas_id_refs_id_07047a89 FOREIGN KEY (personas_id) REFERENCES personas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: recipient_id_refs_id_4811b1f1; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY django_messages_message
    ADD CONSTRAINT recipient_id_refs_id_4811b1f1 FOREIGN KEY (recipient_id) REFERENCES destinatarios(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: respuestas_pregunta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY respuestas
    ADD CONSTRAINT respuestas_pregunta_id_fkey FOREIGN KEY (pregunta_id) REFERENCES comentarios(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: respuestas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY respuestas
    ADD CONSTRAINT respuestas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipo_personal_id_refs_id_aa53b485; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY personal
    ADD CONSTRAINT tipo_personal_id_refs_id_aa53b485 FOREIGN KEY (tipo_personal_id) REFERENCES tipo_personal(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipo_sede_id_refs_id_c2dc3e9a; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT tipo_sede_id_refs_id_c2dc3e9a FOREIGN KEY (tipo_sede_id) REFERENCES tipo_sede(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ubicacion_id_refs_id_5f28c73e; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT ubicacion_id_refs_id_5f28c73e FOREIGN KEY (ubicacion_id) REFERENCES parroquia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: umail
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

