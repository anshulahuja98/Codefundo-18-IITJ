package demo.tensorflow.org.customvision_sample;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

public class DisplayCure extends AppCompatActivity {

    private EditText name;
    private TextView description, cure;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_cure);
        String disease = getIntent().getStringExtra("disease");

        name = findViewById(R.id.editText);
        description = findViewById(R.id.textView);
        cure = findViewById(R.id.textView2);

        name.setText(disease);

        switch (disease) {
            case "Ichthyosis":
                cure.setText("Cure: Antiinflammatory and Vitamin A derivative ");
                description.setText("Ichthyosis is an inherited skin disorder in which dead skin cells accumulate in thick, dry scales on your skin's surface.Most cases of ichthyosis vulgaris are mild, but some are severe. Sometimes other skin diseases, such as the allergic skin condition eczema, are associated with ichthyosis.");
                break;
            case "scabies":
                cure.setText("Cure: Antiparasite");
                description.setText("A contagious, intensely itchy skin condition caused by a tiny, burrowing mite. The most common symptom of scabies is intense itching in the area where the mites burrow. Scabies can be treated by killing the mites and their eggs with medication that's applied from the neck down and left on for eight hours. The mites can also be killed using oral medication. ");
                break;
            case "Eczema":
                cure.setText("Cure: Steroid, Antihistamine, and Topical antiseptic");
                description.setText("Eczema symptoms include itchy, red, and dry skin caused by inflammation. It’s most commonly found in children, although adults can get it. It is also called atopic dermatitis and is treated with oral medications, steroid creams and light therapy .");
                break;
            case "Atopic-Dermatitis":
                cure.setText("Cure: Steroid, Antihistamine, and Topical antiseptic");
                description.setText("Atopic-dermatitis symptoms include itchy, red, and dry skin caused by inflammation. It’s most commonly found in children, although adults can get it. It is treated with oral medications, steroid creams and light therapy .");
                break;
            case "candidiases":
                cure.setText("Cure: Antifungal medication");
                description.setText("A fungal infection typically on the skin or mucous membranes caused by candida.");
                break;
            case "Impetigo(bacteial infection)":
                cure.setText("Cure: Antibiotics");
                description.setText("Classic signs and symptoms of impetigo involve red sores that quickly rupture, ooze for a few days and then form a yellowish-brown crust. The sores usually occur around the nose and mouth but can be spread to other areas of the body by fingers, clothing and towels. Itching and soreness are generally mild.");
                break;
            case "intertrigo":
                cure.setText("Cure: short-term use of a topical steroid");
                description.setText("Intertrigo (intertriginous dermatitis) is an inflammatory condition of skin folds, induced or aggravated by heat, moisture, maceration, friction, and lack of air circulation.");
                break;
            case "cutaneous-Larvae-Migrans":
                cure.setText("Cure: Anthelmintics such as tiabendazole, albendazole, mebendazole and ivermectin are used. ");
                description.setText("Cutaneous larva migrans (abbreviated CLM) is a skin disease in humans, caused by the larvae of various nematode parasites of the hookworm family (Ancylostomatidae)");
            case "Urticaria":
                cure.setText("Cure: Antihistamine, Steroid, Vasoconstrictor, and Anti-Inflammatory");
                description.setText("Hives is a common skin rash triggered by many things, including certain foods, medication and stress.\n" +
                        "Symptoms include itchy, raised, red or skin-coloured welts on the skin's surface.");
            case "keratosis":
                cure.setText("Cure: Freezing, Tissue scraping, and Laser therapy");
                description.setText("A seborrhoeic keratosis is one of the most common non-cancerous skin growths in older adults. While it's possible for one to appear on its own, multiple growths are more common.\n" +
                        "Seborrheic keratosis often appears on the face, chest, shoulders or back. It has a waxy, scaly, slightly elevated appearance");
            case "Tinea ring worm":
                cure.setText("Cure: Antifungal medication");
                description.setText("Ringworm is spread by skin-to-skin contact or by touching an infected animal or object.\n" +
                        "Ringworm is typically scaly and may be red and itchy. Ringworm of the scalp is common in children, where it may cause bald patches.");
            case "Lyme Disease":
                cure.setText("Cure: antibiotic treatment");
                description.setText("Deer ticks can carry the bacteria that cause Lyme disease.\n" +
                        "Lyme disease causes a rash, often in a bull's-eye pattern, and flu-like symptoms. Joint pain and weakness in the limbs can also occur.");
            case  "Common insect bite":
                cure.setText("Cure: Antihistamine, Nonsteroidal anti-Inflammatory drug, and Analgesic");
                description.setText("Most bites cause mild stinging or itching. Some bites can trigger a life-threatening allergic reaction that requires emergency care. Breathing difficulty, facial swelling, dizziness, confusion and hives are symptoms of such a reaction.");
                break;
            default:
                cure.setText("Null");
                description.setText("Null");
                break;
        }
    }
}
