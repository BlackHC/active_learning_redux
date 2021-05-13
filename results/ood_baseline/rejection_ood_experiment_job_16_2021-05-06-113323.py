store = {}
store['timestamp']=1620297203
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=16']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=40
store['config']={'seed': 20, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.356658458709717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.65586519241333})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.664146661758423})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.1264681816101074})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6829, 'crossentropy': 2.0237904296875}
store['active_learning_steps'][0]['acquisition']={'indices': [22605, 57593, 1245, 41553, 11379], 'labels': [0, 5, 5, 0, 0], 'scores': [1.2681613564491272, 1.2284514904022217, 1.2220006585121155, 1.2117546796798706, 1.2019889950752258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.256129741668701})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7226948738098145})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7699337005615234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2159504890441895})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.672, 'crossentropy': 2.0376142578125}
store['active_learning_steps'][1]['acquisition']={'indices': [23347, 25415, 6171, 35044, 42383], 'labels': [8, 8, 5, 8, 8], 'scores': [1.130357801914215, 1.0764211416244507, 1.0703331232070923, 1.0604010820388794, 1.0510252118110657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.0803706645965576})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6150293350219727})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8938698768615723})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.371044158935547})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6581, 'crossentropy': 1.8752767578125}
store['active_learning_steps'][2]['acquisition']={'indices': [26522, 28577, 12223, 55404, 40360], 'labels': [2, 2, 2, 2, 2], 'scores': [1.0506521463394165, 1.0257431268692017, 1.0254282355308533, 1.024196445941925, 1.0230610966682434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.218660593032837})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.390925645828247})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5540852546691895})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7789359092712402})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7145, 'crossentropy': 1.8572142578125}
store['active_learning_steps'][3]['acquisition']={'indices': [42707, 34706, 51314, 28371, 15210], 'labels': [3, 0, 0, 3, 3], 'scores': [1.1025322079658508, 1.1022122502326965, 1.0968331694602966, 1.0939542651176453, 1.0883322358131409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.995107650756836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.3725829124450684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.57649564743042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.782867908477783})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6894, 'crossentropy': 1.8536375}
store['active_learning_steps'][4]['acquisition']={'indices': [42103, 19805, 36, 13593, 5973], 'labels': [6, 6, 6, 6, 6], 'scores': [1.0362887382507324, 1.0239118337631226, 1.0135637521743774, 1.0087833404541016, 1.0015899538993835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8221216201782227})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2531557083129883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.50205659866333})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.6643500328063965})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7381, 'crossentropy': 1.5864693359375}
store['active_learning_steps'][5]['acquisition']={'indices': [2246, 5596, 43288, 57292, 32538], 'labels': [7, 7, 7, 7, 7], 'scores': [1.1098759174346924, 1.109078586101532, 1.0554896593093872, 1.0462431907653809, 1.0294970870018005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.45814847946167})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.8462204933166504})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.7761907577514648})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7955892086029053})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.774, 'crossentropy': 1.257}
store['active_learning_steps'][6]['acquisition']={'indices': [25315, 6418, 52358, 34786, 29339], 'labels': [5, 5, 2, 9, 4], 'scores': [1.0615328550338745, 1.0038837790489197, 1.0037322640419006, 0.9995460510253906, 0.992326021194458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2609546184539795})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4630017280578613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5275648832321167})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6690329313278198})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8002, 'crossentropy': 1.0860818359375}
store['active_learning_steps'][7]['acquisition']={'indices': [3300, 32977, 5191, 29952, 1239], 'labels': [2, 6, 2, 1, 8], 'scores': [1.0157897472381592, 0.987236738204956, 0.9622466564178467, 0.942254900932312, 0.9348436594009399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2857118844985962})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.531692624092102})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.5213582515716553})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.7404727935791016})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7816, 'crossentropy': 1.13129306640625}
store['active_learning_steps'][8]['acquisition']={'indices': [16196, 18370, 18633, 53026, 8493], 'labels': [2, 2, 2, 2, 2], 'scores': [0.9045302867889404, 0.8915485143661499, 0.8765913248062134, 0.8734387159347534, 0.8672734498977661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.106248140335083})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.27958083152771})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3898365497589111})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.374922513961792})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8115, 'crossentropy': 1.0206826171875}
store['active_learning_steps'][9]['acquisition']={'indices': [3653, 36122, 11096, 18405, 5106], 'labels': [9, 9, 9, 9, 9], 'scores': [0.9952677488327026, 0.9836150407791138, 0.9259824752807617, 0.9192503690719604, 0.9118927717208862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.253321886062622})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3164145946502686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5136849880218506})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.408102035522461})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8127, 'crossentropy': 1.05506591796875}
store['active_learning_steps'][10]['acquisition']={'indices': [28226, 29132, 181, 34610, 51498], 'labels': [8, 8, 3, 5, 5], 'scores': [0.972681999206543, 0.9140196442604065, 0.8912358283996582, 0.8902682662010193, 0.8725159764289856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0757349729537964})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.056565523147583})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.309164047241211})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3801567554473877})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4229657649993896})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8413, 'crossentropy': 0.92351435546875}
store['active_learning_steps'][11]['acquisition']={'indices': [2856, 10937, 31014, 50858, 50433], 'labels': [4, 4, 8, 4, 4], 'scores': [1.0697522163391113, 1.0012538433074951, 0.9618179798126221, 0.961338996887207, 0.9561011791229248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0196906328201294})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2879493236541748})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2414350509643555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.338789701461792})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8197, 'crossentropy': 0.925770703125}
store['active_learning_steps'][12]['acquisition']={'indices': [36951, 34485, 22743, 3599, 11202], 'labels': [7, 7, 7, 7, 9], 'scores': [0.8359328508377075, 0.826404869556427, 0.8244348764419556, 0.8144294023513794, 0.811048686504364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0189489126205444})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0377171039581299})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2127232551574707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0888087749481201})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8222, 'crossentropy': 0.92927421875}
store['active_learning_steps'][13]['acquisition']={'indices': [33798, 31684, 45048, 38898, 36508], 'labels': [7, 7, 4, 4, 5], 'scores': [0.8898487687110901, 0.8799760341644287, 0.8756827116012573, 0.8615982532501221, 0.8539886474609375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9790014028549194})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9021904468536377})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0843329429626465})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.044762372970581})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1234164237976074})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.806882763671875}
store['active_learning_steps'][14]['acquisition']={'indices': [20641, 7833, 15487, 20363, 49607], 'labels': [9, 5, 8, 8, 3], 'scores': [1.0606449246406555, 1.037578821182251, 1.0220980048179626, 1.0088419318199158, 0.9630607962608337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8820330500602722})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9021157026290894})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9889580011367798})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.030908226966858})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8521, 'crossentropy': 0.82647158203125}
store['active_learning_steps'][15]['acquisition']={'indices': [2352, 55503, 44040, 10916, 11269], 'labels': [0, 0, 0, 0, 0], 'scores': [0.7559410333633423, 0.7533092498779297, 0.7525274753570557, 0.7517783641815186, 0.7490402460098267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9294964075088501})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9185734987258911})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9803614616394043})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.110353708267212})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0295000076293945})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.869, 'crossentropy': 0.773927685546875}
store['active_learning_steps'][16]['acquisition']={'indices': [19524, 34804, 52801, 14256, 32510], 'labels': [2, 8, 2, 6, 2], 'scores': [1.0214683413505554, 0.9896885752677917, 0.9895601868629456, 0.9809026718139648, 0.9799556136131287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8700963258743286})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8400458097457886})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8839460611343384})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0117853879928589})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.085923433303833})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8721, 'crossentropy': 0.71730771484375}
store['active_learning_steps'][17]['acquisition']={'indices': [15432, 10768, 33426, 29712, 35946], 'labels': [4, 4, 4, 5, 4], 'scores': [0.9741826057434082, 0.9554944038391113, 0.9398923516273499, 0.9362139105796814, 0.9236385226249695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8639236688613892})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.810771644115448})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8311159610748291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9272538423538208})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8820033073425293})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.7090091796875}
store['active_learning_steps'][18]['acquisition']={'indices': [43648, 22083, 21666, 48681, 34429], 'labels': [5, 2, 7, 2, 4], 'scores': [1.013674259185791, 0.9577783942222595, 0.9375672340393066, 0.9310453534126282, 0.9300585985183716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9267908334732056})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7709818482398987})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8016465902328491})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8534834384918213})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8640111088752747})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.722883154296875}
store['active_learning_steps'][19]['acquisition']={'indices': [40589, 51986, 58560, 42020, 28512], 'labels': [2, 2, 0, 9, 5], 'scores': [0.9333627223968506, 0.9206437468528748, 0.9151172041893005, 0.911627471446991, 0.895470142364502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9273589849472046})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8336204290390015})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8259915113449097})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.914371132850647})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0989363193511963})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.948271632194519})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8782, 'crossentropy': 0.76912119140625}
store['active_learning_steps'][20]['acquisition']={'indices': [39222, 224, 509, 9180, 42787], 'labels': [3, 1, 3, 3, 4], 'scores': [0.9249387383460999, 0.9198908805847168, 0.9187942743301392, 0.9146541953086853, 0.9135132431983948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9308514595031738})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7693972587585449})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8065091371536255})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9138017892837524})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8835588693618774})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.883, 'crossentropy': 0.70814501953125}
store['active_learning_steps'][21]['acquisition']={'indices': [28183, 4384, 5474, 18150, 17658], 'labels': [9, 8, 8, 8, 8], 'scores': [0.9636395573616028, 0.9597225189208984, 0.9496853351593018, 0.9458382725715637, 0.9396546483039856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9882112741470337})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7632334232330322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7734075784683228})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7922650575637817})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8448376655578613})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.664547119140625}
store['active_learning_steps'][22]['acquisition']={'indices': [54573, 57392, 20050, 59314, 37696], 'labels': [2, 8, 9, 9, 2], 'scores': [0.962456226348877, 0.9572378993034363, 0.9538081884384155, 0.9526736736297607, 0.9412720799446106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.953116774559021})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.689652681350708})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7280734777450562})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7518249154090881})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7931764721870422})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.633315673828125}
store['active_learning_steps'][23]['acquisition']={'indices': [6684, 42362, 34520, 42703, 33358], 'labels': [0, 0, 6, 0, 9], 'scores': [0.9251502752304077, 0.8949084281921387, 0.8629898726940155, 0.8616584539413452, 0.8612351417541504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8668549060821533})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6697559356689453})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7017021179199219})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7091073989868164})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7269922494888306})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.56882099609375}
store['active_learning_steps'][24]['acquisition']={'indices': [25920, 32427, 22104, 8390, 36998], 'labels': [2, 0, 2, 2, 2], 'scores': [0.9245290756225586, 0.9220049977302551, 0.8933355808258057, 0.8818830251693726, 0.8816237449645996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9061435461044312})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7492014169692993})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7410392761230469})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.883479118347168})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8215093612670898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8312914371490479})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.6450869140625}
store['active_learning_steps'][25]['acquisition']={'indices': [8339, 23140, 8771, 42931, 2381], 'labels': [5, 7, 3, 3, 7], 'scores': [1.0248939990997314, 1.0096112489700317, 1.0086612701416016, 1.0043655633926392, 0.9880938529968262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1020398139953613})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8265198469161987})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.686996579170227})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7859618663787842})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7244249582290649})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8931424021720886})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.626310546875}
store['active_learning_steps'][26]['acquisition']={'indices': [48349, 38598, 13942, 16756, 55743], 'labels': [2, 7, 4, 7, 3], 'scores': [0.937750518321991, 0.9046662449836731, 0.8924481272697449, 0.8826269507408142, 0.877536416053772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9341235160827637})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.635490894317627})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6992251873016357})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7726000547409058})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8548240661621094})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.578759765625}
store['active_learning_steps'][27]['acquisition']={'indices': [33812, 18525, 59309, 22561, 36415], 'labels': [6, 6, 8, 6, 6], 'scores': [0.8589072227478027, 0.842984676361084, 0.8109487295150757, 0.8079087138175964, 0.8027480244636536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9322589635848999})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6757882833480835})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6205066442489624})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6488518714904785})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6820433139801025})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6692681312561035})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.524500146484375}
store['active_learning_steps'][28]['acquisition']={'indices': [25120, 20322, 17756, 39668, 55218], 'labels': [8, 1, 8, 8, 8], 'scores': [0.9789249300956726, 0.9545043110847473, 0.9390833377838135, 0.9327815175056458, 0.9142282605171204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.95531165599823})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6593511700630188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5736712217330933})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6091703176498413})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7530857920646667})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7277360558509827})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.515410107421875}
store['active_learning_steps'][29]['acquisition']={'indices': [52785, 23962, 37048, 3719, 32776], 'labels': [3, 3, 9, 2, 4], 'scores': [0.9577819108963013, 0.9241394400596619, 0.8970975875854492, 0.890204906463623, 0.8860093355178833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0359129905700684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.638821542263031})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6148364543914795})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5832080245018005})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6226440072059631})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6693102121353149})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.723514199256897})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.50795537109375}
store['active_learning_steps'][30]['acquisition']={'indices': [27169, 50317, 52889, 26072, 41933], 'labels': [6, 3, -1, 1, 5], 'scores': [0.9915379285812378, 0.96165531873703, 0.9581624269485474, 0.9491005539894104, 0.922546923160553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.0925168991088867})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6134374141693115})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5927433967590332})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.597877025604248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5894008874893188})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6335756182670593})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6835777759552002})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.655500054359436})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.54080244140625}
store['active_learning_steps'][31]['acquisition']={'indices': [1812, 14201, 15472, 24457, 40595], 'labels': [4, 7, 3, 8, 8], 'scores': [1.0226745009422302, 1.0131699442863464, 0.9857417345046997, 0.9691352844238281, 0.9686422348022461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9521843194961548})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6276169419288635})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5495878458023071})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5278081893920898})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5929745435714722})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5407928228378296})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5919268131256104})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.482518359375}
store['active_learning_steps'][32]['acquisition']={'indices': [37383, 11572, 59726, 32387, 26733], 'labels': [3, 5, 5, 4, 2], 'scores': [1.0434547662734985, 0.9842932224273682, 0.9669504761695862, 0.9484683275222778, 0.9444138407707214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9167273044586182})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6415531039237976})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6394311189651489})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5925901532173157})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5591431856155396})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6286867260932922})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5800294280052185})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6396728754043579})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.482985400390625}
store['active_learning_steps'][33]['acquisition']={'indices': [11292, 5548, 59286, 37469, 27429], 'labels': [1, 8, 8, 2, 0], 'scores': [1.0137364268302917, 0.9859325289726257, 0.9759975671768188, 0.9669843912124634, 0.9603077173233032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9957455396652222})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6358293294906616})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.625822901725769})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5207691192626953})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5300901532173157})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5804179906845093})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.580669105052948})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.489397265625}
store['active_learning_steps'][34]['acquisition']={'indices': [59468, 49364, 36281, 39457, 40712], 'labels': [7, 7, 7, 0, 7], 'scores': [0.963317334651947, 0.9367591142654419, 0.9201166033744812, 0.9122657179832458, 0.9110704362392426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0824693441390991})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5005592107772827})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4767918884754181})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45714524388313293})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45242613554000854})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45489126443862915})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.421613872051239})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5282268524169922})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5475797653198242})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4888501763343811})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.41809560546875}
store['active_learning_steps'][35]['acquisition']={'indices': [20526, 35401, 6818, 42113, 5315], 'labels': [-1, 3, -1, -1, 3], 'scores': [1.0544172525405884, 1.0370437502861023, 1.035974144935608, 1.033791422843933, 1.0140785574913025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.1973674297332764})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6644360423088074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6105773448944092})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5915671586990356})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6387550830841064})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6002562046051025})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6711630821228027})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.542691357421875}
store['active_learning_steps'][36]['acquisition']={'indices': [13003, 57728, 10992, 21532, 23027], 'labels': [-1, 9, -1, 5, -1], 'scores': [1.0249077081680298, 1.0122785568237305, 0.9906558990478516, 0.9820412993431091, 0.9791218042373657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0489318370819092})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5679332613945007})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.510036051273346})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5553938746452332})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4746009111404419})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5103131532669067})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5574050545692444})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49186649918556213})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.48883251953125}
store['active_learning_steps'][37]['acquisition']={'indices': [34328, 49563, 44123, 50736, 7264], 'labels': [8, 8, 8, -1, 9], 'scores': [1.0664311647415161, 0.978249728679657, 0.9657024145126343, 0.9607667922973633, 0.9582829475402832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0918093919754028})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6021460294723511})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5801029205322266})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5386587381362915})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49598705768585205})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5625937581062317})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5926229953765869})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5286888480186462})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.457606005859375}
store['active_learning_steps'][38]['acquisition']={'indices': [40624, 52462, 27540, 34828, 43745], 'labels': [-1, 9, -1, -1, 8], 'scores': [1.0281886458396912, 1.0178255438804626, 0.9959233403205872, 0.9795991778373718, 0.9642219543457031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1205174922943115})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6476055383682251})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5317243337631226})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.604058027267456})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5250219702720642})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.540064811706543})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5614151954650879})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5434737205505371})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.48654814453125}
store['active_learning_steps'][39]['acquisition']={'indices': [34743, 15899, 46021, 46368, 57507], 'labels': [9, 9, 9, 8, 0], 'scores': [1.0230982899665833, 1.0210843682289124, 1.018923580646515, 0.9947484135627747, 0.9780101776123047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.073899745941162})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6155508756637573})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5281403660774231})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5273430347442627})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49838197231292725})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5053293704986572})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5084450244903564})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5349559783935547})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.4525091796875}
store['active_learning_steps'][40]['acquisition']={'indices': [11539, 18487, 53990, 12984, 31958], 'labels': [-1, 4, -1, 8, -1], 'scores': [1.0148299932479858, 0.9867035746574402, 0.9815142154693604, 0.9765979647636414, 0.9595106840133667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1375279426574707})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6035130620002747})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5364670753479004})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49634072184562683})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4257872700691223})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4637303352355957})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4495730996131897})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4835704267024994})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9507, 'crossentropy': 0.3855845703125}
store['active_learning_steps'][41]['acquisition']={'indices': [12986, 50714, 52686, 51180, 52169], 'labels': [5, 8, 5, 7, 2], 'scores': [1.0491538047790527, 1.0239226818084717, 0.986523449420929, 0.9715810716152191, 0.9540074467658997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0523769855499268})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6645953059196472})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5516703724861145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5029370784759521})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5348876118659973})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47937527298927307})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5451271533966064})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5366585850715637})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5287455320358276})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.459654443359375}
store['active_learning_steps'][42]['acquisition']={'indices': [13031, 55244, 41307, 49890, 10044], 'labels': [2, 7, 4, 5, 6], 'scores': [1.0637238025665283, 1.0590996742248535, 1.035054624080658, 1.011275291442871, 1.0010105073451996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1311923265457153})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5801659822463989})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4897305369377136})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4446156919002533})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47112828493118286})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5489891767501831})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48471128940582275})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9476, 'crossentropy': 0.41682236328125}
store['active_learning_steps'][43]['acquisition']={'indices': [57718, 32880, 23642, 2980, 50930], 'labels': [7, 0, 2, 7, 0], 'scores': [0.9151983261108398, 0.8961589932441711, 0.886231541633606, 0.8793191909790039, 0.863082766532898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1543649435043335})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6821812391281128})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5275211334228516})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4798121452331543})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4658041000366211})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4853304326534271})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48073917627334595})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5144720077514648})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.439048095703125}
store['active_learning_steps'][44]['acquisition']={'indices': [9966, 40046, 21353, 19590, 7924], 'labels': [0, 7, 0, 5, 8], 'scores': [0.9968807697296143, 0.9810199737548828, 0.9415337443351746, 0.8989402651786804, 0.8947927355766296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1955885887145996})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6482836008071899})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48813939094543457})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5021121501922607})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4658399820327759})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4792053997516632})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4656778573989868})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4848514497280121})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4660244286060333})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42380228638648987})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48059555888175964})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.567436933517456})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5079145431518555})
store['active_learning_steps'][45]['training']['best_epoch']=10
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.427238037109375}
store['active_learning_steps'][45]['acquisition']={'indices': [24440, 50729, 25873, 2202, 45422], 'labels': [0, 0, 8, 1, 0], 'scores': [1.1375588178634644, 1.1345396637916565, 1.124239206314087, 1.1238261461257935, 1.1188759803771973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1454718112945557})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5903345346450806})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44662773609161377})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46988725662231445})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46486809849739075})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4453524351119995})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5323500037193298})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46454787254333496})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4889519214630127})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.4225509765625}
store['active_learning_steps'][46]['acquisition']={'indices': [20946, 36818, 36744, 41802, 17832], 'labels': [3, 7, 1, 2, 3], 'scores': [1.0208375453948975, 1.0010066628456116, 0.9996353387832642, 0.9952279925346375, 0.9818397164344788]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2685012817382812})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6827685236930847})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5882013440132141})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42825424671173096})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.47878026962280273})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4890824556350708})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42479607462882996})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5334241390228271})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5164929032325745})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4312279224395752})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9467, 'crossentropy': 0.45035927734375}
store['active_learning_steps'][47]['acquisition']={'indices': [53872, 6524, 32276, 7788, 29335], 'labels': [8, 5, 3, 1, 8], 'scores': [1.0053353309631348, 0.9948180019855499, 0.9655536413192749, 0.953669011592865, 0.9522547721862793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2126455307006836})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6239641904830933})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5088624954223633})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47714897990226746})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4343048930168152})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4445452094078064})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4498318135738373})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4258734881877899})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5410017967224121})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5635465383529663})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4840811789035797})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.4157603515625}
store['active_learning_steps'][48]['acquisition']={'indices': [40066, 52889, 20150, 842, 3109], 'labels': [4, -1, 3, 4, 6], 'scores': [1.1426924467086792, 1.1204794645309448, 1.0237591862678528, 1.0208992958068848, 1.0112537145614624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1142603158950806})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5941538214683533})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46596401929855347})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42069166898727417})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4329376816749573})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3910979628562927})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4396933913230896})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41315484046936035})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4269707202911377})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9449, 'crossentropy': 0.38595087890625}
store['active_learning_steps'][49]['acquisition']={'indices': [13969, 13774, 3676, 38275, 5175], 'labels': [3, 2, 2, 2, 4], 'scores': [0.9568988084793091, 0.9241981506347656, 0.9115553498268127, 0.9114753603935242, 0.9082574248313904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.124931812286377})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5514076352119446})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4424790143966675})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40936484932899475})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4104796350002289})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4466724991798401})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40085428953170776})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5045328736305237})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48820388317108154})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39779311418533325})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47654294967651367})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4592829942703247})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44909238815307617})
store['active_learning_steps'][50]['training']['best_epoch']=10
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9499, 'crossentropy': 0.4204875}
store['active_learning_steps'][50]['acquisition']={'indices': [23336, 36408, 20172, 4955, 17855], 'labels': [5, 1, 4, 2, 6], 'scores': [1.060651421546936, 1.0425641536712646, 1.0383777618408203, 1.0300288200378418, 1.0229769945144653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1225790977478027})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6313613653182983})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49031150341033936})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43928003311157227})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47402888536453247})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4756249189376831})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49103567004203796})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.39427978515625}
store['active_learning_steps'][51]['acquisition']={'indices': [2427, 8480, 31046, 28016, 13243], 'labels': [7, 2, 6, 0, 7], 'scores': [0.8524675965309143, 0.8433707356452942, 0.8428414463996887, 0.8410646319389343, 0.8357080817222595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.166451096534729})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6196259260177612})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47459346055984497})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4101703464984894})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.438313752412796})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45822715759277344})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47646281123161316})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.3892822021484375}
store['active_learning_steps'][52]['acquisition']={'indices': [17209, 37689, 42477, 29173, 35399], 'labels': [1, 3, 3, 1, 1], 'scores': [0.9323326945304871, 0.9023448824882507, 0.8740426898002625, 0.8709245324134827, 0.8680121302604675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.149414300918579})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6777393817901611})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.43855661153793335})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39768028259277344})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3702630400657654})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4091741442680359})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4110843241214752})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3837500214576721})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.367363232421875}
store['active_learning_steps'][53]['acquisition']={'indices': [670, 53990, 37583, 19789, 26760], 'labels': [3, -1, -1, -1, 8], 'scores': [0.987311065196991, 0.9671170115470886, 0.9661052227020264, 0.9548949599266052, 0.9520264267921448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0790408849716187})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5203429460525513})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45651641488075256})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34964942932128906})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3765161633491516})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3884757161140442})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3686923682689667})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9531, 'crossentropy': 0.367908349609375}
store['active_learning_steps'][54]['acquisition']={'indices': [55739, 44753, 48824, 53990, 29376], 'labels': [5, 5, -1, -1, -1], 'scores': [0.9281076788902283, 0.921988308429718, 0.8966974020004272, 0.8911028504371643, 0.8739414811134338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0293774604797363})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6093388199806213})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4310210347175598})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3730793595314026})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42804303765296936})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36793094873428345})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43460819125175476})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4006255865097046})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3443966805934906})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40358537435531616})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4101467728614807})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4036898612976074})
store['active_learning_steps'][55]['training']['best_epoch']=9
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3627120361328125}
store['active_learning_steps'][55]['acquisition']={'indices': [37583, 40466, 22272, 39561, 18324], 'labels': [-1, 8, 5, 2, 0], 'scores': [1.0144872069358826, 1.01317897439003, 1.011323869228363, 1.0008372068405151, 0.9954556226730347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1370224952697754})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5917619466781616})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4216768145561218})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.375990092754364})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3747117221355438})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40934234857559204})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3569267988204956})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36182597279548645})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3790140151977539})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40156418085098267})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9545, 'crossentropy': 0.3540787109375}
store['active_learning_steps'][56]['acquisition']={'indices': [1674, 1075, 54181, 42838, 52590], 'labels': [9, 7, 9, 9, -1], 'scores': [0.9990992546081543, 0.9755904674530029, 0.9683933854103088, 0.9546397924423218, 0.9326406717300415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2224328517913818})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6338210105895996})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47963619232177734})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43409013748168945})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43726086616516113})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.46653008460998535})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4100250005722046})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3650304973125458})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4230990409851074})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4296644330024719})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43532705307006836})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3857878173828125}
store['active_learning_steps'][57]['acquisition']={'indices': [52590, 38974, 52889, 4564, 9557], 'labels': [-1, 1, -1, -1, 8], 'scores': [1.0735481977462769, 1.0250971913337708, 1.0210028290748596, 1.0024296045303345, 0.9899210929870605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1827926635742188})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5600659847259521})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41435208916664124})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4102400541305542})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39926230907440186})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36591479182243347})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3761935234069824})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39476004242897034})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37042880058288574})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9577, 'crossentropy': 0.34874814453125}
store['active_learning_steps'][58]['acquisition']={'indices': [42472, 8093, 31608, 26358, 22824], 'labels': [2, 0, 2, 3, 9], 'scores': [0.9542755484580994, 0.952519416809082, 0.9427936673164368, 0.9379655718803406, 0.8994237780570984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2535693645477295})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6180385947227478})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46751418709754944})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41604310274124146})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3639550507068634})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3824976682662964})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38930821418762207})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3786255121231079})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9555, 'crossentropy': 0.3650445068359375}
store['active_learning_steps'][59]['acquisition']={'indices': [43176, 6291, 59747, 45593, 14655], 'labels': [2, 3, 5, 6, 3], 'scores': [0.947928786277771, 0.9398596286773682, 0.9297481775283813, 0.9272847771644592, 0.8965692520141602]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2177584171295166})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5567387342453003})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46224719285964966})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4580085873603821})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4820513129234314})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3925666809082031})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42806488275527954})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44064444303512573})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4934907853603363})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.376154248046875}
store['active_learning_steps'][60]['acquisition']={'indices': [54932, 4822, 15402, 9568, 17478], 'labels': [5, 4, 5, 5, 4], 'scores': [1.0352975130081177, 1.022341012954712, 0.9887531399726868, 0.9733803272247314, 0.9682542085647583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2867510318756104})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6087021827697754})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4608398675918579})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3843541145324707})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4023768901824951})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3726061284542084})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3571561872959137})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36127907037734985})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39490562677383423})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3626653552055359})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.3473449462890625}
store['active_learning_steps'][61]['acquisition']={'indices': [52889, 2682, 19344, 21601, 42774], 'labels': [-1, 8, 7, 1, 4], 'scores': [1.0346639752388, 0.9836761355400085, 0.9438588619232178, 0.9377530217170715, 0.9325188398361206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0732872486114502})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5145407915115356})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43923676013946533})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3725353479385376})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34295976161956787})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3291815221309662})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3481632471084595})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3729744851589203})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3734639883041382})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.323254345703125}
store['active_learning_steps'][62]['acquisition']={'indices': [21636, 5082, 30900, 42866, 52971], 'labels': [2, 0, 5, 2, 2], 'scores': [0.9296025037765503, 0.8830521106719971, 0.8807315230369568, 0.8787712454795837, 0.8773036003112793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.188529133796692})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5446066856384277})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42616045475006104})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3675452470779419})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36999213695526123})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37522292137145996})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36418360471725464})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39093419909477234})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3507998585700989})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35375291109085083})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3845762014389038})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3727026581764221})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.3353512939453125}
store['active_learning_steps'][63]['acquisition']={'indices': [47626, 5063, 32668, 26822, 10746], 'labels': [-1, 9, 9, -1, 9], 'scores': [1.071442723274231, 1.0562012195587158, 1.021104335784912, 0.9964748620986938, 0.9942722916603088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2434194087982178})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6314727067947388})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4433709383010864})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39826107025146484})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3992913067340851})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37200552225112915})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32130926847457886})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37798529863357544})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3350282311439514})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37199339270591736})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.3351648193359375}
store['active_learning_steps'][64]['acquisition']={'indices': [43248, 4153, 16836, 47366, 11074], 'labels': [9, 2, 7, 5, 9], 'scores': [0.9521285891532898, 0.9417940378189087, 0.9251958131790161, 0.9151185750961304, 0.9146237969398499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3183716535568237})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5776311755180359})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46211400628089905})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42265772819519043})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4047316014766693})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3909348249435425})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40345925092697144})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36632925271987915})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.40712210536003113})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3597260117530823})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42584723234176636})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4308308959007263})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44618403911590576})
store['active_learning_steps'][65]['training']['best_epoch']=10
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.3593249755859375}
store['active_learning_steps'][65]['acquisition']={'indices': [21990, 8693, 49543, 45800, 20110], 'labels': [1, 3, 8, 9, 4], 'scores': [1.0687421560287476, 1.0191380381584167, 0.9984001517295837, 0.9881597459316254, 0.9868676662445068]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1396234035491943})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6477476358413696})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48232144117355347})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3845837414264679})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3923856317996979})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3760095536708832})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3895615339279175})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3728327751159668})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39217013120651245})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40707606077194214})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4145053029060364})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9507, 'crossentropy': 0.387324462890625}
store['active_learning_steps'][66]['acquisition']={'indices': [7984, 32393, 21896, 47626, 3634], 'labels': [4, 5, 8, -1, 5], 'scores': [1.0457687973976135, 1.0145439505577087, 1.0050727725028992, 1.0039754509925842, 0.9801985919475555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.2333582639694214})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.633298397064209})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4786681532859802})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.373174786567688})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38867491483688354})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3785043954849243})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4153803586959839})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.3774128662109375}
store['active_learning_steps'][67]['acquisition']={'indices': [36268, 9340, 59681, 53990, 56561], 'labels': [5, 5, 0, -1, -1], 'scores': [0.8637506365776062, 0.8296366930007935, 0.8264249563217163, 0.8187364935874939, 0.8161901831626892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1585724353790283})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6089369058609009})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4978467524051666})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4531351923942566})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3814905285835266})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38062363862991333})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37627142667770386})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3877926468849182})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3708718419075012})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.396604984998703})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42917072772979736})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39517101645469666})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.3410916015625}
store['active_learning_steps'][68]['acquisition']={'indices': [46088, 13754, 49222, 47626, 52889], 'labels': [6, -1, 3, -1, -1], 'scores': [1.0885193943977356, 1.0386877059936523, 1.0297350883483887, 1.0005509853363037, 0.994564950466156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4384536743164062})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6780279874801636})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4811505973339081})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4538356065750122})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4560149013996124})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39216023683547974})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4127589762210846})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39708971977233887})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38508832454681396})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38841089606285095})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3934754729270935})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4143705368041992})
store['active_learning_steps'][69]['training']['best_epoch']=9
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3737230224609375}
store['active_learning_steps'][69]['acquisition']={'indices': [58422, 5536, 52889, 57972, 19546], 'labels': [9, 8, -1, 4, 9], 'scores': [0.9837831854820251, 0.9785301089286804, 0.975497841835022, 0.9751865267753601, 0.9721355438232422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2535784244537354})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5978506803512573})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49096405506134033})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42254728078842163})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3680623769760132})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38247150182724})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36617857217788696})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3871803879737854})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3798905611038208})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3610985279083252})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38941633701324463})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36798617243766785})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38024166226387024})
store['active_learning_steps'][70]['training']['best_epoch']=10
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.35627255859375}
store['active_learning_steps'][70]['acquisition']={'indices': [20169, 33338, 39778, 59701, 43823], 'labels': [4, 8, 8, 5, 8], 'scores': [1.0154162645339966, 0.9868952631950378, 0.9855720400810242, 0.9719584584236145, 0.9647244811058044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.247443675994873})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6260151267051697})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4728904366493225})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3999568819999695})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38734328746795654})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39007842540740967})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32978498935699463})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4186450242996216})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39254316687583923})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37861794233322144})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.3383600341796875}
store['active_learning_steps'][71]['acquisition']={'indices': [48360, 40624, 50371, 30359, 28930], 'labels': [3, -1, 7, 7, 7], 'scores': [0.9240861535072327, 0.9228555560112, 0.9004583954811096, 0.8875520825386047, 0.8776503205299377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1755328178405762})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5772885084152222})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40901798009872437})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37208274006843567})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3537101745605469})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29760223627090454})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29560795426368713})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3131495714187622})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.342676043510437})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31778842210769653})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.29652060546875}
store['active_learning_steps'][72]['acquisition']={'indices': [52889, 22497, 20170, 4741, 6347], 'labels': [-1, 7, 9, 6, 3], 'scores': [0.9484575986862183, 0.9133018851280212, 0.8949320912361145, 0.8896204233169556, 0.8852598667144775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.202429175376892})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6416826248168945})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4643961787223816})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4343961477279663})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3656769394874573})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.356537401676178})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3389379382133484})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34820398688316345})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36675530672073364})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31968820095062256})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4128935933113098})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37499043345451355})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34644466638565063})
store['active_learning_steps'][73]['training']['best_epoch']=10
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3327613037109375}
store['active_learning_steps'][73]['acquisition']={'indices': [42428, 52590, 39411, 28368, 52889], 'labels': [5, -1, 2, 9, -1], 'scores': [1.1049599647521973, 1.0157237648963928, 1.0089938640594482, 1.0068126320838928, 0.9925273656845093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2519593238830566})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6113949418067932})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4069405794143677})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38972944021224976})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38532960414886475})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35690081119537354})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32976099848747253})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3892453908920288})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.361907422542572})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36935847997665405})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.3316863037109375}
store['active_learning_steps'][74]['acquisition']={'indices': [52294, 47845, 46658, 52949, 54885], 'labels': [0, 5, 8, 4, 6], 'scores': [1.001087248325348, 0.9514122009277344, 0.9302392601966858, 0.9158905744552612, 0.9144742488861084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2695560455322266})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.63520348072052})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46887409687042236})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3994002938270569})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38997650146484375})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35196739435195923})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3503172993659973})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3327934741973877})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35045963525772095})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37487703561782837})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3642737865447998})
store['active_learning_steps'][75]['training']['best_epoch']=8
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3399556396484375}
store['active_learning_steps'][75]['acquisition']={'indices': [15771, 47220, 11482, 27503, 9396], 'labels': [5, 6, 8, 2, 2], 'scores': [0.9530053734779358, 0.9244957566261292, 0.911622941493988, 0.9037884771823883, 0.8962833285331726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2476325035095215})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6794223785400391})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47998395562171936})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3863377273082733})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3864445090293884})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.363183856010437})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39025843143463135})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3731594681739807})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3961068391799927})
store['active_learning_steps'][76]['training']['best_epoch']=6
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.329704541015625}
store['active_learning_steps'][76]['acquisition']={'indices': [52889, 47626, 27540, 57052, 5271], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9214305281639099, 0.8931350111961365, 0.879027783870697, 0.8788506388664246, 0.8787707686424255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2790889739990234})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6517459154129028})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4575870633125305})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39102041721343994})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37377163767814636})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3807811737060547})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3603065311908722})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3293488025665283})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39997974038124084})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33432796597480774})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3365395665168762})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.324962451171875}
store['active_learning_steps'][77]['acquisition']={'indices': [34847, 40494, 9687, 29903, 43811], 'labels': [0, 0, 0, 0, 0], 'scores': [1.0739137530326843, 1.0085620284080505, 1.0077597498893738, 0.9709750413894653, 0.9628961086273193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3623480796813965})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7028371095657349})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4983091354370117})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4096994996070862})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4017011225223541})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36150234937667847})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3403184413909912})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3799194097518921})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3373543620109558})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3385639488697052})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3769396245479584})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3500105142593384})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.36046767578125}
store['active_learning_steps'][78]['acquisition']={'indices': [18501, 31293, 683, 7638, 59081], 'labels': [4, 8, -1, 8, -1], 'scores': [0.9869937896728516, 0.9797357320785522, 0.9669744968414307, 0.9658768177032471, 0.9566969275474548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.216536045074463})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6561406254768372})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.46709388494491577})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38190606236457825})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35099539160728455})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3716973066329956})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36373621225357056})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32547247409820557})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3533574938774109})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.312620609998703})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3388711214065552})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3314666748046875})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34075868129730225})
store['active_learning_steps'][79]['training']['best_epoch']=10
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.32606240234375}
store['active_learning_steps'][79]['acquisition']={'indices': [31014, 4557, 18307, 41169, 42326], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.0395200848579407, 1.0175892114639282, 0.9882497787475586, 0.9839498996734619, 0.9679614901542664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3040655851364136})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6389214992523193})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4615430235862732})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38328057527542114})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3353419303894043})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3340688943862915})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3280830979347229})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32354336977005005})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35210224986076355})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3714104890823364})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3497294485569})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.340161083984375}
store['active_learning_steps'][80]['acquisition']={'indices': [4379, 4074, 2782, 274, 45171], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0396692156791687, 1.0264267921447754, 0.9950969219207764, 0.9886366128921509, 0.9818445444107056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.437304973602295})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7276202440261841})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4767446517944336})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4247838854789734})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33325621485710144})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3118360638618469})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32479140162467957})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29099398851394653})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31735748052597046})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3061721920967102})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.298268586397171})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.3071414794921875}
store['active_learning_steps'][81]['acquisition']={'indices': [14690, 33162, 45171, 54316, 22139], 'labels': [8, 8, -1, 6, 2], 'scores': [0.9345356822013855, 0.912150502204895, 0.9044685363769531, 0.899776041507721, 0.8903220295906067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3507202863693237})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6716340780258179})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4699259400367737})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3624376654624939})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34372979402542114})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33339089155197144})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3008415699005127})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29807209968566895})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30461791157722473})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.337656170129776})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3373919725418091})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.3020091552734375}
store['active_learning_steps'][82]['acquisition']={'indices': [41453, 56457, 50431, 52516, 48824], 'labels': [3, 3, 3, 6, -1], 'scores': [0.9138195514678955, 0.9089369177818298, 0.8980412483215332, 0.8951228857040405, 0.8912913799285889]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3919169902801514})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6937241554260254})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5424688458442688})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.457732617855072})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3579252064228058})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3507794737815857})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36752134561538696})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3536103367805481})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34684526920318604})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3699359595775604})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3426315188407898})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.379843145608902})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35414713621139526})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36010444164276123})
store['active_learning_steps'][83]['training']['best_epoch']=11
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9599, 'crossentropy': 0.329652001953125}
store['active_learning_steps'][83]['acquisition']={'indices': [52889, 2782, 46995, 47626, 50555], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1166038513183594, 1.0706275701522827, 1.0488130450248718, 1.0145866870880127, 1.0108903646469116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2999622821807861})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6992083191871643})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5343430042266846})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42546743154525757})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3876434564590454})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.369171679019928})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.384966641664505})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3592202961444855})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4019601345062256})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3907390832901001})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33780384063720703})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3609685003757477})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3700646758079529})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3875252902507782})
store['active_learning_steps'][84]['training']['best_epoch']=11
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.3339731689453125}
store['active_learning_steps'][84]['acquisition']={'indices': [52889, 6440, 37692, 57276, 7949], 'labels': [-1, 3, 3, 8, -1], 'scores': [1.0680924654006958, 1.042882263660431, 0.9975452423095703, 0.976714015007019, 0.9548330903053284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3049147129058838})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7074084877967834})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4762546420097351})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36275017261505127})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3984077572822571})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3760277330875397})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36439770460128784})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.3709557861328125}
store['active_learning_steps'][85]['acquisition']={'indices': [54994, 9147, 5740, 36072, 12305], 'labels': [6, 4, 9, 2, 9], 'scores': [0.7602009773254395, 0.7337490320205688, 0.7325233817100525, 0.7215839624404907, 0.7124406099319458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4235949516296387})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7545931935310364})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4379214644432068})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4133104979991913})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4125044643878937})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3561473488807678})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31541115045547485})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29414159059524536})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3088012635707855})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3055272698402405})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3448556363582611})
store['active_learning_steps'][86]['training']['best_epoch']=8
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.3176214599609375}
store['active_learning_steps'][86]['acquisition']={'indices': [30884, 52590, 36126, 53054, 29320], 'labels': [2, -1, 5, -1, 1], 'scores': [1.0257847309112549, 0.9338112473487854, 0.9300153255462646, 0.910982608795166, 0.908183217048645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.252481460571289})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5583025813102722})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41244804859161377})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.367045521736145})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3199685513973236})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3110124468803406})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3395068049430847})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3044824004173279})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3075951337814331})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3495936989784241})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32274162769317627})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.32195888671875}
store['active_learning_steps'][87]['acquisition']={'indices': [45602, 2782, 46995, 29376, 38142], 'labels': [5, -1, -1, -1, 8], 'scores': [1.0713236331939697, 0.9912617206573486, 0.9831420183181763, 0.9640399813652039, 0.9514875411987305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4096471071243286})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7012922763824463})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5489301681518555})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.377083957195282})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3875197172164917})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32822009921073914})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33903568983078003})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3261489272117615})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.300744891166687})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3319172263145447})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3138565123081207})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3359254002571106})
store['active_learning_steps'][88]['training']['best_epoch']=9
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.287835595703125}
store['active_learning_steps'][88]['acquisition']={'indices': [31252, 48102, 4564, 635, 7325], 'labels': [5, 7, -1, 5, 0], 'scores': [0.9453062415122986, 0.9265069961547852, 0.9107130169868469, 0.8855908513069153, 0.8826680779457092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4755330085754395})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7299610376358032})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4918864965438843})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3837713599205017})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39697641134262085})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35638850927352905})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32067450881004333})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3338279128074646})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36548125743865967})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3305727243423462})
store['active_learning_steps'][89]['training']['best_epoch']=7
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.318169091796875}
store['active_learning_steps'][89]['acquisition']={'indices': [52889, 53844, 2845, 32323, 2782], 'labels': [-1, 5, 8, 5, -1], 'scores': [0.8892329931259155, 0.8817839622497559, 0.8723076581954956, 0.8458011746406555, 0.8455898761749268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2940664291381836})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.6229125261306763})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4736722707748413})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3228961229324341})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32254254817962646})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28469938039779663})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29464974999427795})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.287533700466156})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26961749792099})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3058014512062073})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25207000970840454})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3042614161968231})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2713700234889984})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29836931824684143})
store['active_learning_steps'][90]['training']['best_epoch']=11
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.275587646484375}
store['active_learning_steps'][90]['acquisition']={'indices': [22029, 45171, 8202, 2782, 34678], 'labels': [-1, -1, 2, -1, 8], 'scores': [1.0371957421302795, 1.0201335549354553, 0.9944510459899902, 0.9740217328071594, 0.9706839919090271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.534426212310791})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8208811283111572})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5055426359176636})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3490214943885803})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3669349253177643})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3109124004840851})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3397488594055176})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2986316680908203})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3448532819747925})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3061932325363159})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3443514108657837})
store['active_learning_steps'][91]['training']['best_epoch']=8
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.303359521484375}
store['active_learning_steps'][91]['acquisition']={'indices': [52590, 14896, 20903, 38657, 41233], 'labels': [-1, 8, 3, 3, 3], 'scores': [1.0183166861534119, 0.9675349593162537, 0.9388428926467896, 0.9359948039054871, 0.9112163782119751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.4032378196716309})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6699768304824829})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.46903297305107117})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35253190994262695})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3150291442871094})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3528696298599243})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3066965341567993})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2934207618236542})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27248674631118774})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35362356901168823})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2923544645309448})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30613791942596436})
store['active_learning_steps'][92]['training']['best_epoch']=9
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.264285888671875}
store['active_learning_steps'][92]['acquisition']={'indices': [4564, 32918, 52889, 56196, 47626], 'labels': [-1, 2, -1, -1, -1], 'scores': [1.010902762413025, 1.0099136233329773, 0.9788815975189209, 0.9566930532455444, 0.9423507452011108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3629001379013062})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.724215030670166})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4653496742248535})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3723934292793274})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33793649077415466})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31903913617134094})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32491207122802734})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29687076807022095})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3280765414237976})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30181679129600525})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2974032759666443})
store['active_learning_steps'][93]['training']['best_epoch']=8
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.301105029296875}
store['active_learning_steps'][93]['acquisition']={'indices': [52889, 4564, 22098, 45749, 33150], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0821561813354492, 1.0209590792655945, 0.9878057241439819, 0.9562513828277588, 0.9365727305412292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3667685985565186})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7096274495124817})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45525893568992615})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4467657804489136})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3565882742404938})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35855603218078613})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37616342306137085})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3028745651245117})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35912466049194336})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36206457018852234})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3418307900428772})
store['active_learning_steps'][94]['training']['best_epoch']=8
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.3063114013671875}
store['active_learning_steps'][94]['acquisition']={'indices': [52889, 36337, 49541, 21204, 22098], 'labels': [-1, 3, 9, 5, -1], 'scores': [1.097478210926056, 0.9743231534957886, 0.9387512803077698, 0.9299997091293335, 0.9267306923866272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3095757961273193})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.7326576113700867})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.45164692401885986})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3560551404953003})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37007200717926025})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3388497531414032})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3300235867500305})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.354012131690979})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30996066331863403})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2775576710700989})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2853243947029114})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2980601489543915})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.324055016040802})
store['active_learning_steps'][95]['training']['best_epoch']=10
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.279085107421875}
store['active_learning_steps'][95]['acquisition']={'indices': [22098, 45944, 52889, 46995, 54814], 'labels': [-1, 9, -1, -1, 4], 'scores': [1.039609670639038, 0.9756850600242615, 0.9369438290596008, 0.9144464135169983, 0.9098541736602783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3999767303466797})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6287214756011963})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4292376637458801})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3354302644729614})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3344869017601013})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29213961958885193})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27349695563316345})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2812148630619049})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3142896890640259})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.315975159406662})
store['active_learning_steps'][96]['training']['best_epoch']=7
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2734845458984375}
store['active_learning_steps'][96]['acquisition']={'indices': [4379, 52914, 53990, 50736, 32583], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.8746603727340698, 0.8616296052932739, 0.851828396320343, 0.8485455513000488, 0.8474259376525879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4136302471160889})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7366389036178589})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.45176512002944946})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34867122769355774})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32111191749572754})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3205835223197937})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28703072667121887})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29830896854400635})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2978368401527405})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2967086732387543})
store['active_learning_steps'][97]['training']['best_epoch']=7
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.312491650390625}
store['active_learning_steps'][97]['acquisition']={'indices': [30692, 58832, 31512, 52889, 7851], 'labels': [3, 3, 2, -1, 8], 'scores': [0.8935246467590332, 0.8870474100112915, 0.8859536647796631, 0.8683441877365112, 0.8513895869255066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3477556705474854})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6935415863990784})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5007699728012085})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3896058201789856})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34704869985580444})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.321540892124176})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31420689821243286})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32712453603744507})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3100817799568176})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30701297521591187})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.320098340511322})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2812161445617676})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32744985818862915})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3399123549461365})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3578779101371765})
store['active_learning_steps'][98]['training']['best_epoch']=12
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.280087353515625}
store['active_learning_steps'][98]['acquisition']={'indices': [31014, 58445, 52889, 36990, 1518], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.11577707529068, 1.0787432193756104, 1.0764095187187195, 1.0757824778556824, 1.0677809119224548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3744844198226929})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7511811256408691})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4773615598678589})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41711053252220154})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3409741520881653})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.331917941570282})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3119964003562927})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3256053924560547})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3224179744720459})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33516746759414673})
store['active_learning_steps'][99]['training']['best_epoch']=7
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.3062498291015625}
store['active_learning_steps'][99]['acquisition']={'indices': [17382, 52889, 13714, 40624, 46613], 'labels': [6, -1, 4, -1, 4], 'scores': [1.0334713459014893, 0.9009288549423218, 0.894430935382843, 0.883708655834198, 0.8782517910003662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3490427732467651})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7847484946250916})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4715937077999115})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40598374605178833})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3474721908569336})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3509765863418579})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.356497585773468})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31880393624305725})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3065670132637024})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3457508683204651})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3175164461135864})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3189244270324707})
store['active_learning_steps'][100]['training']['best_epoch']=9
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.3099723876953125}
store['active_learning_steps'][100]['acquisition']={'indices': [517, 26568, 44732, 38249, 29711], 'labels': [8, -1, 6, 8, 8], 'scores': [0.9905179142951965, 0.9892139434814453, 0.9664522409439087, 0.9620990753173828, 0.9552263021469116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.230414867401123})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6899864673614502})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.45577001571655273})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35772526264190674})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3064568042755127})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3034699559211731})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2903200387954712})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2972489595413208})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29553014039993286})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3003653287887573})
store['active_learning_steps'][101]['training']['best_epoch']=7
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2830928955078125}
store['active_learning_steps'][101]['acquisition']={'indices': [47036, 37078, 12211, 52889, 25246], 'labels': [2, 8, 3, -1, 2], 'scores': [0.9158675074577332, 0.877614438533783, 0.8755810260772705, 0.8672663569450378, 0.8596860468387604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3942973613739014})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7723244428634644})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.47115039825439453})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3925824761390686})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3680000901222229})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32100600004196167})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30491793155670166})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29278120398521423})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28976354002952576})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28304624557495117})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2881081700325012})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3242475986480713})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28287845849990845})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30266985297203064})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2796069383621216})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2639757990837097})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30134332180023193})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2606922388076782})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3447067141532898})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27849364280700684})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29750269651412964})
store['active_learning_steps'][102]['training']['best_epoch']=18
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2675340576171875}
store['active_learning_steps'][102]['acquisition']={'indices': [45171, 16063, 38080, 34739, 7949], 'labels': [-1, -1, 2, 9, -1], 'scores': [1.0973913669586182, 1.0487828254699707, 1.0376204252243042, 1.0374671816825867, 1.0343493223190308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4523242712020874})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7941727638244629})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.49785348773002625})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38282251358032227})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3714538812637329})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34295886754989624})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2988801598548889})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2687300145626068})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31131258606910706})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.258634477853775})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.350464403629303})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3285706639289856})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30561625957489014})
store['active_learning_steps'][103]['training']['best_epoch']=10
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2892048828125}
store['active_learning_steps'][103]['acquisition']={'indices': [15779, 21700, 2782, 52889, 7949], 'labels': [0, 7, -1, -1, -1], 'scores': [0.9716314673423767, 0.9676209688186646, 0.9482079744338989, 0.9459362030029297, 0.9245179891586304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.3211462497711182})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6702632904052734})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4787869453430176})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3860130310058594})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37661510705947876})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37731730937957764})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30948343873023987})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3090519607067108})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3090323805809021})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2999517321586609})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3554168939590454})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2934035062789917})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3373955488204956})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3686296343803406})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.3009408712387085})
store['active_learning_steps'][104]['training']['best_epoch']=12
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2959014404296875}
store['active_learning_steps'][104]['acquisition']={'indices': [42673, 57322, 46975, 29161, 34828], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0831989645957947, 1.0808985233306885, 1.0601969957351685, 1.0468670725822449, 1.0383421778678894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.4175682067871094})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6827936768531799})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4908919036388397})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3957398533821106})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3320029079914093})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3429686427116394})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27614715695381165})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26928213238716125})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3194715976715088})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30085116624832153})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2758767008781433})
store['active_learning_steps'][105]['training']['best_epoch']=8
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.292147509765625}
store['active_learning_steps'][105]['acquisition']={'indices': [26568, 40624, 49573, 47626, 40654], 'labels': [-1, -1, 2, -1, 5], 'scores': [1.0985904932022095, 1.000176191329956, 0.9858149290084839, 0.9827146530151367, 0.9452008605003357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.487766981124878})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.8141326904296875})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6228469610214233})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4077155590057373})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34746044874191284})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3302105665206909})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29118871688842773})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30424201488494873})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27162113785743713})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2955608665943146})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2841859459877014})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31927037239074707})
store['active_learning_steps'][106]['training']['best_epoch']=9
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2750357666015625}
store['active_learning_steps'][106]['acquisition']={'indices': [52889, 53990, 11357, 40624, 34828], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.041477620601654, 1.0226120352745056, 0.9895771145820618, 0.9892414808273315, 0.9877434372901917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4021737575531006})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.787145733833313})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5003235340118408})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3989261984825134})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3321360945701599})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30091017484664917})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31068265438079834})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32364892959594727})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2853110432624817})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30641239881515503})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29676681756973267})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29737281799316406})
store['active_learning_steps'][107]['training']['best_epoch']=9
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2897498779296875}
store['active_learning_steps'][107]['acquisition']={'indices': [40624, 52889, 31014, 50736, 33301], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1666551232337952, 1.1348052620887756, 1.0943505764007568, 1.0913647413253784, 1.081914246082306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5611740350723267})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.7160358428955078})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5374187231063843})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41253575682640076})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3988502025604248})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3544057309627533})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40343570709228516})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.32987964153289795})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3025525212287903})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3378028869628906})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3553585112094879})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30145537853240967})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30531758069992065})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3079413175582886})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3345356583595276})
store['active_learning_steps'][108]['training']['best_epoch']=12
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.30213115234375}
store['active_learning_steps'][108]['acquisition']={'indices': [17792, 31014, 11643, 14894, 36990], 'labels': [9, -1, 5, 5, -1], 'scores': [0.9881170988082886, 0.9795181155204773, 0.9668517112731934, 0.9665877819061279, 0.9639073014259338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5763429403305054})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6872866153717041})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5018843412399292})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4797751307487488})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33302736282348633})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3699912428855896})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3192853331565857})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3178325891494751})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2797597050666809})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29951539635658264})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2807141840457916})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31901752948760986})
store['active_learning_steps'][109]['training']['best_epoch']=9
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2852618408203125}
store['active_learning_steps'][109]['acquisition']={'indices': [22029, 28536, 18598, 52889, 40549], 'labels': [-1, 3, 9, -1, -1], 'scores': [0.9604296684265137, 0.8935044407844543, 0.8801076412200928, 0.8796800374984741, 0.8785051107406616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5074254274368286})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6940385103225708})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5183998346328735})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.427315890789032})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33539915084838867})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3054961860179901})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2971060276031494})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29900896549224854})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28355199098587036})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3068845868110657})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2560151219367981})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3070676326751709})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27863621711730957})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26088154315948486})
store['active_learning_steps'][110]['training']['best_epoch']=11
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.975, 'crossentropy': 0.2673594482421875}
store['active_learning_steps'][110]['acquisition']={'indices': [3762, 47297, 15366, 12651, 52889], 'labels': [8, 8, 8, 9, -1], 'scores': [0.9685267210006714, 0.9533716440200806, 0.9454344511032104, 0.9451020956039429, 0.9372472763061523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.2714968919754028})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6755949258804321})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5002374053001404})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37728485465049744})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33577945828437805})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3271941542625427})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.336153507232666})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2911621928215027})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3470866084098816})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3323197364807129})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3086276650428772})
store['active_learning_steps'][111]['training']['best_epoch']=8
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2892798828125}
store['active_learning_steps'][111]['acquisition']={'indices': [52590, 22029, 29751, 35384, 46393], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.001436471939087, 0.9659054279327393, 0.9557827115058899, 0.9030208587646484, 0.9013172388076782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5364665985107422})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7929221391677856})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5348595380783081})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4138709008693695})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3456726670265198})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37109461426734924})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29747849702835083})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3018324077129364})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33840733766555786})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30672213435173035})
store['active_learning_steps'][112]['training']['best_epoch']=7
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.309529443359375}
store['active_learning_steps'][112]['acquisition']={'indices': [7949, 11377, 8170, 52889, 20036], 'labels': [-1, 3, 7, -1, 1], 'scores': [0.9321454763412476, 0.9021214842796326, 0.8675328493118286, 0.8273917436599731, 0.8269699811935425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4450242519378662})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7545550465583801})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5010840892791748})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39511191844940186})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32992422580718994})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3466249108314514})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3097688555717468})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2817176580429077})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2857019305229187})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2739596962928772})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3019132614135742})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29274922609329224})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29756009578704834})
store['active_learning_steps'][113]['training']['best_epoch']=10
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2827455078125}
store['active_learning_steps'][113]['acquisition']={'indices': [52590, 52889, 59081, 45171, 35384], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0911523699760437, 1.0449780225753784, 1.0390759706497192, 1.0064457058906555, 0.9961607456207275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.4980380535125732})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.8211349248886108})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.518855631351471})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.40670138597488403})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38256555795669556})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3380456566810608})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3154562711715698})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36431658267974854})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3275192081928253})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.30864378809928894})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3298115134239197})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.28652042150497437})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2957422435283661})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2889421582221985})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3302052319049835})
store['active_learning_steps'][114]['training']['best_epoch']=12
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2878546875}
store['active_learning_steps'][114]['acquisition']={'indices': [52889, 47626, 43560, 8228, 42438], 'labels': [-1, -1, 5, 3, 9], 'scores': [1.0186980366706848, 1.0109044909477234, 0.9633190035820007, 0.944545328617096, 0.9389927387237549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3053452968597412})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6869723200798035})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6129894256591797})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3996502161026001})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33253777027130127})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29181528091430664})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28412652015686035})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2763022780418396})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29570963978767395})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3116069436073303})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3193798065185547})
store['active_learning_steps'][115]['training']['best_epoch']=8
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2860409912109375}
