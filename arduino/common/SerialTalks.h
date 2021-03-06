#ifndef __SERIALTALKS_H__
#define __SERIALTALKS_H__

// This library is free software from Club robot Insa Rennes sources; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.

#include <Arduino.h>
#include "serialutils.h"
#include "CRC16.h"

#ifndef SERIALTALKS_BAUDRATE
#define SERIALTALKS_BAUDRATE 115200 /*!< Bauderate utiliser */
#endif

#ifndef SERIALTALKS_INPUT_BUFFER_SIZE
#define SERIALTALKS_INPUT_BUFFER_SIZE 64
#endif

#ifndef SERIALTALKS_OUTPUT_BUFFER_SIZE
#define SERIALTALKS_OUTPUT_BUFFER_SIZE 64
#endif

#ifndef SERIALTALKS_UUID_ADDRESS
#define SERIALTALKS_UUID_ADDRESS 0x0000000000
#endif

#ifndef SERIALTALKS_UUID_LENGTH
#define SERIALTALKS_UUID_LENGTH 32
#endif

#ifndef SERIALTALKS_MAX_PROCESSING
#define SERIALTALKS_MAX_PROCESSING 0x4
#endif

#ifndef SERIALTALKS_MAX_OPCODE
#define SERIALTALKS_MAX_OPCODE 0x20
#endif

#define SERIALTALKS_MASTER_BYTE 'R'
#define SERIALTALKS_SLAVE_BYTE 'A'

#define SERIALTALKS_DEFAULT_UUID_LENGTH 9

#define SERIALTALKS_RESEVED_OPCODE_0 0X0
#define SERIALTALKS_RESEVED_OPCODE_1 0X1
#define SERIALTALKS_RESEVED_OPCODE_2 0X2
#define SERIALTALKS_RESEVED_OPCODE_3 0X3
#define SERIALTALKS_RESEVED_OPCODE_4 0X4
#define SERIALTALKS_RESEVED_OPCODE_5 0X5
#define SERIALTALKS_RESEVED_OPCODE_6 0X6
#define SERIALTALKS_RESEVED_OPCODE_7 0X7
#define SERIALTALKS_RESEVED_OPCODE_8 0X8
#define SERIALTALKS_RESEVED_OPCODE_9 0X9

#define SERIALTALKS_PING_OPCODE (SERIALTALKS_RESEVED_OPCODE_0)
#define SERIALTALKS_GETUUID_OPCODE (SERIALTALKS_RESEVED_OPCODE_1)
#define SERIALTALKS_SETUUID_OPCODE (SERIALTALKS_RESEVED_OPCODE_2)
#define SERIALTALKS_DISCONNECT_OPCODE (SERIALTALKS_RESEVED_OPCODE_3)
#define SERIALTALKS_GETEEPROM_OPCODE (SERIALTALKS_RESEVED_OPCODE_4)
#define SERIALTALKS_SETEEPROM_OPCODE (SERIALTALKS_RESEVED_OPCODE_5)
#define SERIALTALKS_GETBUFFERSIZE_OPCODE (SERIALTALKS_RESEVED_OPCODE_6)
#define SERIALTALKS_RESEND_OPCODE 0xFE
#define SERIALTALKS_FREE_BUFFER_OPCODE 0xFA
#define SERIALTALKS_STDOUT_RETCODE 0xFFFFFFFF
#define SERIALTALKS_STDERR_RETCODE 0xFFFFFFFE

#define SERIALTALKS_CRC_SIZE 2
/** class SerialTalks
 *  \brief Object de communication serial avec un ordinateur.
 *	\author Ulysse Darmet
	\author Fran??ois Gauthier-Clerc
 *  est un outil permettant ?? l'arduino de pouvoir r??pondre aux requ??tes recu depuis le serial.
 *  Il utilise donc le port serial (usb) pour envoyer ou recevoir des donn??es avec l'ordinateur ou la raspberry
 *  La classe est capable de lancer des methodes sur demande de l'ordinateur ou de la raspberry.
 */
class SerialTalks
{
public: // Public API
    /** class ostream
	 * \brief Stream virtuel pour les erreurs et autre.
	 *	est un outils pour permettre de mieux transmettre les erreurs rencontr??es et les STD::OUT
	*/
    class ostream : public Print
    {
    public:
        //! Ecrit sur le serial l'octet indiqu??.
        /*!
			\param c octet ?? passer dans le serial.
			\return Nombre d'octet transmit.
		*/
        virtual size_t write(uint8_t);
        //! Ecrit sur le serial le buffer indiqu?? (liste d'octets).
        /*!
			\param buffer ?? passer.
			\param size (taille) du buffer.
			\return Nombre d'octet transmit.
		*/
        virtual size_t write(const uint8_t *buffer, size_t size);
        //! Surcharge de l'op??rateur '<<'.
        //! Cette m??thode permet de passer plus facilement les objets dans le serial avec conversion en octets automatique.
        /*!
			\param object ?? passer dans le serial.

		*/
        template <typename T>
        ostream &operator<<(const T &object)
        {
            print(object);
            return *this;
        }

    protected:
        //! Initialise le ostream. C'est ?? dire expliciter le pointeur du SerialTalks et le retcode ?? associer.
        /*!
			\param parent SerialTalks ?? associer.
			\param retcode Code d'identification ?? utiliser pour l'utilisation du serial.

		*/
        void begin(SerialTalks &parent, long retcode);

        SerialTalks *m_parent; /*!< SerialTalks parent  */
        long m_retcode;        /*!< RetCode ?? associer au flux virtuel */

        friend class SerialTalks;
    };
    /*! \var typedef *Instruction
	 * \brief Instruction est un pointeur de fonction dont la signature doit ??tre de la forme : (SerialTalks& inst, Deserializer& input, Serializer& output).
	 *
	 */
    typedef void (*Instruction)(SerialTalks &inst, Deserializer &input, Serializer &output);
    /*! \var typedef *Processing
	 * \brief Processing est un pointeur de fonction dont la signature doit ??tre de la forme : (SerialTalks& inst, Deserializer& input).
	 *	Cette m??thode sera appel??e apr??s que la raspberry traitera la requ??te de l'arduino.
	 */
    typedef void (*Processing)(SerialTalks &inst, Deserializer &input);
    //! Initialise le SerialTalks avec un Stream d'<arduino.h>.
    /*!
		\param stream Flux ?? associer pour la communication de SerialTalks.
	*/
    void begin(Stream &stream);
    //! Associe une Instruction ?? un OPCODE.
    /*!
		\param opcode Code ?? associer ?? la fonction.
		\param instruction Fonction ?? r??pertorier dans SerialTalks.
	*/
    void bind(byte opcode, Instruction instruction);
    //! Associe une fonction au retour de la requ??te de l'OPCODE.
    /*!
		\param opcode Code ?? associer ?? la fonction.
		\param instruction Fonction ?? r??pertorier dans SerialTalks.
	*/
    void attach(byte opcode, Processing processing);
    //! Lance la fonction ?? partir des octets re??us. La m??thode lit l'OPCode et transmet ?? la bonne fonction l'objet Deserializer avec le reste les octets re??u non trait??s et un Serialiser pour la r??ponse ?? transmettre.
    /*!
		\param inputBuffer Liste des octets re??us pour cette requ??te.
		\return Vrai si la fonction ?? renvoy?? des informations.
	*/
    bool execinstruction(byte *inputBuffer);
    //! Lit les octets re??us et les traites quand ils forment une requ??te compl??te.
    /*!
		\return Vrai si une requ??te ?? renvoy?? une information.
	*/

    bool execute();

    /**
	 * @brief R??cup??re le Serializer pour le remplir avant l'appel de la m??thode SerialTalks::send.
	 * 
	 * @return Serializer ?? remplir. 
	 */
    Serializer getSerializer() { return Serializer(m_outputBuffer); }

    /**
	 * @brief Lance la requ??te avec les donn??es charg??es dans le Serializer et l'OPCODE.
	 * 
	 * @param opcode Code ?? utiliser pour le requ??te vers la Raspeberry.
	 * @param output Serializer ?? utiliser pour r??cuperer les donn??es.
	 * @return int  Nombre d'octet envoy??s.
	 */
    int send(byte opcode, Serializer output);

    //! Indique si le stream de SerialTalks est bien connect??.
    /*!
		\return Vrai si le stream est connect??.
	*/
    bool isConnected() const { return m_connected; }
    //! M??thode bloquante jusqu'a la connexion du Stream ou jusqu'au timeout.
    /*!
		\param timeout Timeout pour la m??thode 
		\return Vrai si le Stream est connect??.
	*/
    bool waitUntilConnected(float timeout = -1);
    //! Ecrit sur le pointeur l'UUID enregistr?? dans l'EEPROM de l'Arduino.
    /*!
		\param uuid Pointeur ?? utiliser.
		\return Vrai si il existe bien un UUID.
	*/
    bool getUUID(char *uuid);
    //! Enregistre l'UUID dans l'EEPROM de l'Arduino.
    /*!
		\param uuid Pointeur de l'UUID ?? enregistrer.
	*/
    void setUUID(const char *uuid);
    //! G??n??re un UUID
    /*!
		\param uuid Pointeur pour renvoyer l'UUID.
		\param length Longueur en octet de l'UUID ?? g??n??rer.
	*/
    static void generateRandomUUID(char *uuid, int length);

    // Public attributes (yes we dare!)

    ostream out; /*!< Flux virtuel pour les STD:OUT.  */
    ostream err; /*!< Flux virtuel pour les STD:ERR ou erreur.  */

protected: // Protected methods
    int sendback(long retcode, const byte *buffer, int size);

    /**
	 * @brief M??thode interme pour traiter les retours de requ??tes.
	 * 
	 * @param inputBuffer 
	 * @return true 
	 * @return false 
	 */
    bool receive(byte *inputBuffer);

    // Attributes

    Stream *m_stream; /*!< Stream de communication utilis?? par SerialTalks.*/
    bool m_connected; /*!< Repr??sente l'??tat de connection.*/

    Instruction m_instructions[SERIALTALKS_MAX_OPCODE]; /*!< Listes des instructions enregistr??es avec un OPCode associ??.*/
    Processing m_processings[SERIALTALKS_MAX_PROCESSING];
    ; /*!< Listes des instructions de retour enregistr??es avec un OPCode associ??.*/

    byte m_inputBuffer[SERIALTALKS_INPUT_BUFFER_SIZE];   /*!< Buffer d'entr??e d'informations.*/
    byte m_outputBuffer[SERIALTALKS_OUTPUT_BUFFER_SIZE]; /*!< Buffer de sortie d'informations.  */

    enum //     m_state
    {
        SERIALTALKS_WAITING_STATE,               ///<En attente de l'arriv?? d'un octet.
        SERIALTALKS_INSTRUCTION_STARTING_STATE,  ///< En attente du prochain octet de la requ??te correspondant ?? la taille de celle-ci.
        SERIALTALKS_CRC_RECIEVING_STATE,         ///< En attente du hash d'int??grit??.
        SERIALTALKS_INSTRUCTION_RECEIVING_STATE, ///< R??ception des derniers octet de la requ??te.
    } m_state;                                   /// Diff??rents ??tats de r??ception.

    enum // m_order
    {
        SERIALTALKS_ORDER,  ///< Requ??te re??u de la raspberry.
        SERIALTALKS_RETURN, ///< Retour de requ??te.
    } m_order;              /// Type de requ??te re??u.

    byte m_bytesNumber;  /*!< Variable pour la r??ception de donn??es qui correspond ?? la longueur de la requ??te en bytes (valeur donn??e dans le deuxi??me byte d'une requ??te).*/
    byte m_bytesCounter; /*!< Variable d'incrementation pour la r??ception de donn??es.*/
    long m_lastTime;     /*!< Timeout pour la r??ception d'octets d'une m??me requ??te.*/
    unsigned long m_lastRetcode;
    // for cyclic redundancy check
    CRC16 m_crc;

    byte m_crcBytesCounter;
    uint16_t received_crc_value;

    byte m_crc_tab[SERIALTALKS_CRC_SIZE + 1];
    byte m_crc_tmp[SERIALTALKS_OUTPUT_BUFFER_SIZE];

private:
    /**
	 * @brief M??thode interne pour demander le r??envoie de la requ??te.
	 * 
	 */
    void launchResend(void);
    /**
	 * @brief Indique ?? la Raspberry que le buffer est vide.
	 */
    void freeBuffer(void);

    //! M??thode pour la requ??te de ping.
    static void PING(SerialTalks &talks, Deserializer &input, Serializer &output);
    //! M??thode pour la requ??te d'UUID.
    static void GETUUID(SerialTalks &talks, Deserializer &input, Serializer &output);
    //! M??thode pour la requ??te de changement d'UUID.
    static void SETUUID(SerialTalks &talks, Deserializer &input, Serializer &output);
    //! M??thode pour lire dans l'EEPROM.
    static void GETEEPROM(SerialTalks &talks, Deserializer &input, Serializer &output);
    //! M??thode pour ??cire dans l'EEPROM.
    static void SETEEPROM(SerialTalks &talks, Deserializer &input, Serializer &output);
    //! M??thode pour r??cuperer la taille du Buffer.
    static void GETBUFFERSIZE(SerialTalks &talks, Deserializer &input, Serializer &output);
};

extern SerialTalks talks;

#endif // __SERIALTALKS_H__
