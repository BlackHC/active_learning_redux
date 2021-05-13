store = {}
store['timestamp']=1620259375
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=18']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=40
store['config']={'seed': 22, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4040708541870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8182177543640137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8356027603149414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.934849739074707})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6696, 'crossentropy': 2.2352109375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 49247], ['id', 19924], ['id', 22862], ['id', 35772], ['id', 40417], ['id', 5163], ['ood', 19698], ['id', 39410], ['id', 49849], ['id', 46036], ['id', 9437], ['id', 12751], ['id', 30439], ['id', 31344], ['id', 53106], ['id', 21115], ['id', 29126], ['id', 20525], ['id', 59363], ['id', 48321]], 'labels': [2, 0, 7, 8, 8, 8, 8, 5, 7, 2, 9, 7, 0, 5, 6, 5, 8, 4, 0, 3], 'scores': [0.9478341341018677, 0.6848783493041992, 0.7148743271827698, 0.6883037686347961, 0.7300988435745239, 0.9985219836235046, 0.5996787548065186, 0.9315974712371826, 0.940116822719574, 1.197777509689331, 1.1467434167861938, 0.9221588373184204, 0.9427806735038757, 1.0579389333724976, 0.8806418776512146, 0.9962955713272095, 0.93228679895401, 0.6373013854026794, 0.8040554523468018, 0.9798222184181213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3164801597595215})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.450819730758667})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.7251924276351929})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.8894524574279785})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7473, 'crossentropy': 1.32011533203125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 48292], ['id', 49038], ['id', 59368], ['id', 6274], ['id', 25406], ['ood', 6588], ['id', 14737], ['id', 27557], ['id', 44308], ['id', 35784], ['id', 48509], ['id', 25662], ['id', 32876], ['id', 4143], ['id', 55958], ['id', 18947], ['id', 4509], ['id', 31506], ['id', 3910], ['id', 18405]], 'labels': [2, 5, 5, 5, 2, 1, 5, 5, 8, 5, 8, 4, 6, 6, 5, 5, 2, 2, 6, 9], 'scores': [0.6871688961982727, 0.7941931486129761, 0.7636181712150574, 0.6738874316215515, 0.6390421390533447, 0.4544084072113037, 0.7265154719352722, 0.8638187646865845, 0.6635797023773193, 0.7006304264068604, 0.7877922654151917, 0.8086082339286804, 0.6651241779327393, 0.7675154805183411, 0.8721292018890381, 0.8056577444076538, 0.6837088465690613, 0.512234091758728, 0.786909818649292, 0.8072860836982727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0731289386749268})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3626389503479004})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.32735013961792})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.452221155166626})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.8087, 'crossentropy': 0.98866611328125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 22238], ['id', 41072], ['id', 20015], ['id', 30954], ['id', 21786], ['id', 36899], ['id', 22092], ['id', 46187], ['ood', 12703], ['id', 34646], ['id', 33583], ['id', 30464], ['id', 1364], ['id', 53554], ['ood', 41778], ['id', 42209], ['id', 33939], ['id', 13742], ['id', 57300], ['id', 49060]], 'labels': [3, 5, 8, 4, 9, 3, 3, 3, 7, 3, 3, 4, 9, 3, 5, 9, 3, 9, 3, 6], 'scores': [0.4729766845703125, 0.638607919216156, 0.8432559967041016, 0.6657105088233948, 0.7208577394485474, 0.6636883020401001, 0.6276354789733887, 0.6845013499259949, 0.4360361099243164, 0.7043046951293945, 0.721021831035614, 0.6225391626358032, 0.7635728120803833, 0.8542242050170898, 0.5193345546722412, 0.6626960039138794, 0.5742693543434143, 0.7965681552886963, 0.661026120185852, 0.6745373010635376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9890514016151428})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.070216417312622})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9982643127441406})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0837030410766602})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8226, 'crossentropy': 0.9643009765625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 14349], ['id', 20911], ['id', 29534], ['id', 33001], ['id', 51084], ['id', 26863], ['id', 23629], ['id', 24533], ['id', 39708], ['id', 7181], ['id', 39169], ['id', 4116], ['id', 7582], ['id', 13736], ['id', 57625], ['id', 52484], ['id', 57517], ['id', 49315], ['id', 32511], ['id', 23671]], 'labels': [4, 0, 5, 5, 7, 2, 5, 8, 2, 0, 1, 7, 3, 3, 3, 7, 1, 7, 5, 5], 'scores': [0.4553952217102051, 0.452991247177124, 0.5367395877838135, 0.6432263851165771, 0.5277584791183472, 0.5541930198669434, 0.5756120681762695, 0.5634810924530029, 0.5437719821929932, 0.4265581965446472, 0.4585188627243042, 0.6529558897018433, 0.4549804925918579, 0.4081774353981018, 0.6069003939628601, 0.47460198402404785, 0.45920896530151367, 0.5322389006614685, 0.47187912464141846, 0.5680125951766968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7278820276260376})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6919324398040771})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.606197714805603})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6026885509490967})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6455550193786621})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.674432635307312})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6885336637496948})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.603140771484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 31335], ['id', 57985], ['id', 18003], ['id', 10260], ['id', 14901], ['ood', 9259], ['id', 49824], ['id', 39096], ['id', 2381], ['id', 26966], ['id', 28637], ['id', 13905], ['id', 46379], ['ood', 46434], ['id', 23807], ['id', 974], ['id', 12594], ['id', 29259], ['ood', 38318], ['id', 49021]], 'labels': [5, 4, 2, 3, 2, 9, 8, 9, 7, 7, 5, 7, 3, 5, 9, 9, 8, 8, 5, 2], 'scores': [0.874650239944458, 0.6931596994400024, 0.8578936457633972, 0.9005519151687622, 0.6922333538532257, 0.42649686336517334, 1.0455104112625122, 0.4262707233428955, 0.6827243864536285, 0.8477230370044708, 0.7895320653915405, 0.7768740653991699, 0.6949798464775085, 0.7114347219467163, 0.7168780565261841, 0.6553894281387329, 0.7774230241775513, 0.8041468858718872, 0.8817948698997498, 0.7735713720321655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.778643786907196})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5940556526184082})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5858603715896606})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.598073422908783})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6125101447105408})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6266078948974609})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.515258935546875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 55743], ['id', 54296], ['id', 57404], ['id', 1295], ['id', 24898], ['id', 14740], ['id', 57728], ['id', 32668], ['id', 5679], ['id', 4066], ['id', 7768], ['id', 10916], ['id', 20840], ['id', 15992], ['id', 25879], ['id', 50612], ['id', 17581], ['id', 4955], ['id', 49188], ['id', 12345]], 'labels': [3, 3, 8, 3, 9, 4, 9, 9, 3, 1, 8, 0, 0, 0, 8, 6, 0, 2, 3, 3], 'scores': [0.7119846343994141, 0.7388312220573425, 0.6640989780426025, 0.7735191583633423, 0.6586171388626099, 0.49323052167892456, 0.7729517221450806, 0.6978098750114441, 0.8647156953811646, 0.8052725195884705, 0.640862226486206, 0.9954519867897034, 0.9453293085098267, 0.9358499646186829, 0.5712956190109253, 0.5436718463897705, 0.6939175724983215, 0.9006110429763794, 0.5962698757648468, 0.8033215403556824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.859155535697937})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5532403588294983})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5235202312469482})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5401858687400818})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5582534074783325})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5286286473274231})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.5014623046875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 26072], ['id', 39480], ['id', 21112], ['id', 31464], ['id', 37115], ['id', 17658], ['id', 38381], ['id', 70], ['id', 14791], ['id', 3200], ['id', 15763], ['id', 47185], ['id', 33505], ['id', 28371], ['id', 51407], ['id', 25246], ['id', 34608], ['id', 2184], ['id', 17706], ['id', 5480]], 'labels': [1, 9, 3, 6, 9, 8, 2, 1, 8, 2, 1, 9, 2, 3, 6, 2, 9, 2, 1, 2], 'scores': [0.8878843784332275, 0.5530645847320557, 0.5664156675338745, 0.5564302802085876, 0.455711305141449, 0.587726354598999, 0.5756411850452423, 0.6500047445297241, 0.8621531128883362, 0.5016636848449707, 0.5037897825241089, 0.6226809024810791, 0.7702475786209106, 0.7546567320823669, 0.6314226984977722, 0.6532061100006104, 0.7952556014060974, 0.566055953502655, 0.5480643510818481, 0.4966120719909668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8637757301330566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5812138319015503})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4971557855606079})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5002289414405823})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5319141149520874})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5264127254486084})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.466562158203125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 40905], ['id', 33031], ['ood', 14331], ['id', 36363], ['id', 16488], ['id', 48753], ['id', 46869], ['id', 29872], ['id', 53242], ['id', 5936], ['id', 19371], ['id', 27624], ['id', 53032], ['id', 20172], ['id', 32262], ['id', 370], ['id', 19923], ['id', 34912], ['id', 51508], ['id', 23140]], 'labels': [5, 4, 3, 6, 9, 8, 6, 6, 7, 4, 8, 6, 4, 4, 4, 7, 4, 8, 6, 7], 'scores': [0.7546404004096985, 0.695580005645752, 0.3031890392303467, 0.7947428226470947, 0.7279694676399231, 0.5914098024368286, 0.543324887752533, 0.8343295454978943, 0.5502411127090454, 0.6438934803009033, 0.5812593698501587, 0.786255419254303, 0.5866304039955139, 0.6650581359863281, 0.6701569557189941, 0.6699888706207275, 0.8237524628639221, 0.7102829217910767, 0.5683227777481079, 0.9470656514167786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8803941607475281})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5567290782928467})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4307132363319397})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.43559175729751587})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5153305530548096})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5036599636077881})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.4174359375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 57276], ['id', 21426], ['id', 16036], ['id', 38389], ['id', 17012], ['id', 33338], ['id', 41540], ['id', 3012], ['id', 11514], ['id', 17079], ['id', 52345], ['id', 57427], ['id', 26738], ['ood', 58360], ['id', 4638], ['id', 58537], ['id', 57435], ['id', 56464], ['id', 27537], ['id', 28423]], 'labels': [8, 6, 8, 7, 1, 8, 2, 0, 0, 6, 2, 2, 4, 9, 3, 5, 0, 9, 2, 0], 'scores': [0.5497318506240845, 0.6338850855827332, 0.7623196840286255, 0.5976290702819824, 0.5468128323554993, 0.5830963253974915, 0.5818649530410767, 0.750213623046875, 0.45432326197624207, 0.6921847462654114, 0.7952285408973694, 0.5573238134384155, 0.6535893082618713, 0.38926851749420166, 0.5218542218208313, 0.3564137816429138, 0.5395383834838867, 0.6892439723014832, 0.4832501709461212, 0.35154926776885986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8531104326248169})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5332434177398682})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4245647192001343})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40912193059921265})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4540579915046692})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41627317667007446})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4129631519317627})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9523, 'crossentropy': 0.3718558349609375}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 38827], ['id', 6466], ['id', 19495], ['id', 52169], ['id', 29286], ['id', 43262], ['id', 20820], ['id', 9158], ['id', 33796], ['id', 48577], ['id', 36452], ['id', 40646], ['id', 3060], ['id', 16022], ['id', 6604], ['id', 41188], ['id', 2636], ['id', 29712], ['id', 33340], ['id', 37016]], 'labels': [0, 2, 3, 2, 9, 5, 9, 0, 7, 9, 5, 8, 7, 8, 8, 6, 8, 5, 5, 5], 'scores': [0.5129001140594482, 0.739485502243042, 0.8143170475959778, 0.818160891532898, 0.4133356213569641, 0.7950758934020996, 1.0156719088554382, 0.6399802565574646, 0.6206198334693909, 0.626384973526001, 0.8387755155563354, 0.6910647749900818, 0.5731657147407532, 0.9629291892051697, 1.0413256883621216, 0.5994096398353577, 0.9006470441818237, 0.644305944442749, 0.7388243675231934, 0.532913088798523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0497504472732544})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5164627432823181})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.422573447227478})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.405997633934021})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36493396759033203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44881466031074524})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.392586350440979})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.403011679649353})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9519, 'crossentropy': 0.358926171875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 16084], ['id', 34231], ['id', 15949], ['id', 3720], ['id', 3688], ['id', 31512], ['id', 7923], ['id', 14825], ['id', 39942], ['id', 29834], ['id', 52130], ['id', 52462], ['id', 4111], ['id', 966], ['id', 32417], ['id', 14008], ['id', 48355], ['id', 37584], ['id', 24820], ['id', 54880]], 'labels': [5, 7, 5, 0, 8, 2, 8, 3, 9, 5, 0, 9, 2, 3, 9, 8, 3, 5, 5, 5], 'scores': [0.8588857650756836, 0.44870203733444214, 0.861033022403717, 0.5158125758171082, 0.45897358655929565, 0.629498690366745, 0.943726658821106, 0.9075857996940613, 0.7986502051353455, 1.0182923078536987, 0.8586244583129883, 0.883679211139679, 0.7702627182006836, 0.8348594903945923, 0.5484656691551208, 0.6193754076957703, 0.6483533084392548, 1.0506882071495056, 0.7506702542304993, 0.724433422088623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9765211343765259})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48817121982574463})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42019712924957275})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38105326890945435})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3926994800567627})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37437376379966736})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43386197090148926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42954376339912415})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4169425368309021})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.3474131103515625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 13018], ['id', 52548], ['id', 30952], ['id', 6309], ['id', 58543], ['id', 37486], ['id', 31917], ['id', 7224], ['id', 36408], ['id', 52168], ['id', 22193], ['id', 16644], ['id', 31284], ['id', 7284], ['id', 8284], ['id', 56066], ['id', 25159], ['id', 17131], ['id', 13388], ['id', 35326]], 'labels': [8, 2, 7, 3, 8, 2, 9, 6, 1, 3, 5, 7, 7, 7, 0, 7, 0, 3, 3, 5], 'scores': [0.563413679599762, 0.8129817843437195, 0.5030876994132996, 0.7747411131858826, 0.8172570466995239, 0.45174840092658997, 0.7033193707466125, 0.784134566783905, 0.6593856811523438, 0.7530935406684875, 0.7062373161315918, 0.7009477615356445, 0.5406038761138916, 0.7214608192443848, 0.6160345077514648, 0.7101828455924988, 0.8860063552856445, 0.5430924892425537, 0.7718728184700012, 0.7134793996810913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9403563737869263})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6082558035850525})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3927384614944458})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39047306776046753})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39680373668670654})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38427209854125977})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40354278683662415})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42723292112350464})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39701250195503235})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.338024560546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 14749], ['id', 6636], ['id', 39778], ['id', 2202], ['id', 35649], ['id', 3336], ['id', 8435], ['id', 34252], ['id', 57311], ['id', 14373], ['id', 49822], ['id', 52092], ['id', 40766], ['id', 1674], ['id', 3268], ['id', 50728], ['id', 9804], ['id', 45975], ['id', 58129], ['id', 29886]], 'labels': [0, 5, 8, 1, 3, 3, 5, 2, 5, 2, 8, 7, 4, 9, 6, 3, 1, 0, 9, 8], 'scores': [0.8278892636299133, 0.7490260004997253, 0.8138453960418701, 0.6510654091835022, 0.5914101600646973, 0.902964174747467, 0.5774835348129272, 0.7749178409576416, 0.6807516813278198, 0.649251401424408, 0.43157950043678284, 0.8886302709579468, 0.5881036520004272, 0.8340436816215515, 0.6707807183265686, 0.7776259183883667, 0.8610386252403259, 0.6950743794441223, 0.7392054200172424, 0.869592010974884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9694914817810059})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4801574647426605})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39840877056121826})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38500258326530457})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33410200476646423})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3326575756072998})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3399233818054199})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3299509286880493})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3713354170322418})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36253446340560913})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35975414514541626})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.27923291015625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 55060], ['id', 34495], ['id', 52294], ['id', 24943], ['id', 18796], ['id', 36409], ['id', 12778], ['id', 22083], ['id', 49890], ['id', 32091], ['id', 4850], ['id', 17494], ['id', 41618], ['id', 49616], ['ood', 3932], ['id', 35232], ['id', 28412], ['id', 52686], ['ood', 48160], ['id', 34829]], 'labels': [5, 2, 0, 3, 3, 3, 8, 2, 5, 3, 3, 5, 5, 7, 8, 8, 0, 5, 0, 5], 'scores': [0.5991746187210083, 0.6006112098693848, 1.0340169668197632, 0.6730522513389587, 0.5166862308979034, 0.95409095287323, 0.5800339579582214, 0.9464698433876038, 1.0537890195846558, 0.6746858358383179, 0.6683499217033386, 0.9417844414710999, 0.7128773331642151, 0.8365803062915802, 0.67305588722229, 0.7943169474601746, 0.6349811553955078, 0.5588089823722839, 0.615684986114502, 0.9293858408927917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1065013408660889})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5239458680152893})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4526406228542328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3751460313796997})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36480820178985596})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3469788432121277})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3695743680000305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3853762447834015})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3648332357406616})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.323098876953125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 42989], ['id', 37794], ['id', 53133], ['id', 44904], ['id', 12686], ['id', 29320], ['id', 36268], ['id', 34819], ['id', 21880], ['id', 41573], ['id', 29476], ['id', 58138], ['id', 52927], ['id', 42703], ['id', 27358], ['id', 29132], ['id', 43059], ['id', 788], ['id', 44157], ['id', 14976]], 'labels': [0, 4, 8, 4, 0, 1, 5, 8, 2, 3, 3, 8, 1, 0, 8, 8, 0, 9, 3, 4], 'scores': [0.6988205909729004, 0.7134011387825012, 0.6078630089759827, 0.5833775997161865, 0.6555827856063843, 0.6589191555976868, 0.7328271269798279, 0.7489256858825684, 0.8604393601417542, 0.674616277217865, 0.5358840823173523, 0.6555486917495728, 0.521124541759491, 0.9209166169166565, 0.7589552998542786, 0.7376773357391357, 0.699491024017334, 0.8303542137145996, 0.5600317716598511, 0.4452281594276428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9242545366287231})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5511448979377747})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4184120297431946})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32747453451156616})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3010851740837097})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3268142342567444})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31209421157836914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3477940559387207})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.299819970703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48098], ['id', 10588], ['id', 13985], ['id', 32178], ['id', 16989], ['id', 13942], ['id', 19253], ['id', 28930], ['id', 21174], ['id', 41453], ['ood', 35239], ['id', 54885], ['id', 35004], ['ood', 55864], ['id', 20363], ['id', 56457], ['id', 18193], ['id', 22149], ['id', 16209], ['id', 48360]], 'labels': [7, 9, 1, 4, 2, 4, 8, 7, 2, 3, 5, 6, 9, 5, 8, 3, 9, 3, 2, 3], 'scores': [0.44456034898757935, 0.356952965259552, 0.4610719680786133, 0.6116546988487244, 0.779923141002655, 0.5880545973777771, 0.6310628056526184, 0.8405748009681702, 0.6544472575187683, 0.7532647848129272, 0.3282686471939087, 0.7238262891769409, 0.44263923168182373, 0.5345928072929382, 0.47920501232147217, 0.7783124446868896, 0.39022648334503174, 0.6423576474189758, 0.46648597717285156, 0.8266945481300354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0454928874969482})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6058536767959595})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4455496072769165})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36315101385116577})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35561424493789673})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3194230794906616})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33381760120391846})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29538631439208984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3603058457374573})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33762723207473755})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36080431938171387})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2741368896484375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 6220], ['id', 47225], ['id', 22824], ['id', 3470], ['id', 33212], ['id', 35624], ['id', 3644], ['id', 57702], ['id', 39464], ['id', 50431], ['id', 38275], ['id', 14790], ['id', 4907], ['id', 41714], ['id', 41993], ['id', 42450], ['id', 6310], ['id', 59747], ['id', 6765], ['id', 14096]], 'labels': [4, 3, 9, 2, 9, 4, 1, 7, 9, 3, 2, 9, 7, 4, 4, 6, 9, 5, 9, 5], 'scores': [0.6248520016670227, 0.5504144430160522, 0.5133370757102966, 0.8255255818367004, 0.555523157119751, 0.5464836955070496, 0.7728501558303833, 0.7374314665794373, 0.5834248065948486, 0.7423369288444519, 0.8732168674468994, 0.7545416951179504, 0.45715540647506714, 0.8916844129562378, 0.4620458781719208, 0.653766930103302, 0.5973911285400391, 0.8198362588882446, 0.3711344599723816, 0.7436367273330688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.943618655204773})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5150820016860962})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37595003843307495})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35942843556404114})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29346293210983276})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3083958625793457})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.312563419342041})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29594534635543823})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2900370361328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 39373], ['id', 42143], ['id', 46412], ['id', 30861], ['id', 12840], ['id', 50618], ['id', 15450], ['id', 36810], ['id', 8940], ['id', 45344], ['id', 33335], ['id', 48115], ['id', 45056], ['id', 50826], ['id', 29827], ['ood', 32229], ['id', 52644], ['id', 30011], ['id', 13376], ['id', 49082]], 'labels': [8, 6, 0, 4, 9, 6, 6, 6, 6, 5, 7, 8, 8, 2, 4, 8, 7, 3, 3, 3], 'scores': [0.48673492670059204, 0.4765357971191406, 0.6418696045875549, 0.590041995048523, 0.5240261554718018, 0.7212432026863098, 0.5526505708694458, 0.6713013648986816, 0.699817955493927, 0.6170230507850647, 0.42582881450653076, 0.5798336267471313, 0.7527280449867249, 0.6295596361160278, 0.5709879994392395, 0.4386482238769531, 0.6896123290061951, 0.7221202254295349, 0.8053449988365173, 0.5803566575050354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.112455129623413})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5823649764060974})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45843982696533203})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3735194802284241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3286930024623871})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3216989040374756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31447333097457886})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3160628080368042})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.302346408367157})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32012939453125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3040581941604614})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30627718567848206})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.27485947265625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 11960], ['id', 23255], ['id', 29560], ['id', 41999], ['id', 47243], ['id', 44862], ['id', 57642], ['id', 54646], ['id', 43006], ['id', 57334], ['id', 15510], ['id', 18720], ['id', 54848], ['id', 43532], ['id', 51764], ['id', 51618], ['id', 13760], ['id', 45185], ['id', 12305], ['id', 43636]], 'labels': [3, 1, 0, 0, 1, 0, 0, 6, 1, 7, 2, 7, 2, 8, 5, 0, 6, 7, 9, 4], 'scores': [0.7382822036743164, 0.7947012186050415, 0.6641745567321777, 0.8324741721153259, 0.5694034099578857, 0.6094048619270325, 0.5424028635025024, 0.5166035294532776, 0.5332854986190796, 0.5782800316810608, 0.6691973805427551, 0.7520054578781128, 0.5020032525062561, 0.5616408586502075, 0.987056314945221, 0.7685819864273071, 0.9239221811294556, 0.6821801662445068, 0.8461481928825378, 0.7060615420341492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1644566059112549})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5301049947738647})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40923672914505005})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34267115592956543})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3386727571487427})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3313385844230652})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3174968361854553})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2811543345451355})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31612372398376465})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28714045882225037})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3157329559326172})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2580561279296875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 57054], ['id', 10064], ['id', 26544], ['id', 12321], ['id', 22513], ['id', 50236], ['id', 5295], ['id', 35464], ['id', 18487], ['id', 20236], ['id', 340], ['id', 54909], ['id', 43823], ['id', 20614], ['id', 54316], ['id', 14787], ['id', 23886], ['id', 10285], ['id', 33426], ['id', 52727]], 'labels': [8, 8, 4, 0, 7, 0, 4, 9, 4, 4, 7, 8, 8, 8, 6, 9, 1, 1, 4, 4], 'scores': [0.643271803855896, 0.689846932888031, 0.606534481048584, 0.6738125085830688, 0.6886524558067322, 0.6445815563201904, 0.8067366480827332, 0.6695345640182495, 0.8517271280288696, 0.6507152318954468, 0.6433354616165161, 0.4774109125137329, 0.7045760154724121, 0.6841449737548828, 0.6816526353359222, 0.6229425668716431, 0.5711703300476074, 0.5313106775283813, 0.771412193775177, 0.7781246900558472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0297895669937134})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5037088394165039})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38693803548812866})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3364984393119812})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27439165115356445})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27981334924697876})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2838040888309479})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2815752625465393})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2605222900390625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 4564], ['id', 49463], ['id', 37319], ['id', 7867], ['id', 2958], ['id', 27051], ['id', 34016], ['ood', 35596], ['id', 24479], ['id', 24513], ['id', 26132], ['id', 32338], ['id', 36348], ['id', 38920], ['id', 7984], ['id', 33982], ['id', 32747], ['id', 49354], ['ood', 5880], ['id', 10014]], 'labels': [4, 0, 8, 6, 8, 8, 0, 9, 8, 2, 4, 1, 9, 7, 4, 2, 8, 0, 7, 7], 'scores': [0.5095621943473816, 0.7739201188087463, 0.5377675294876099, 0.5712984204292297, 0.7430668473243713, 0.646368682384491, 0.5343539714813232, 0.29781150817871094, 0.5971013903617859, 0.5387540459632874, 0.5309023857116699, 0.531209409236908, 0.609872043132782, 0.6093564033508301, 0.7809618711471558, 0.5036212801933289, 0.6770243644714355, 0.6781424283981323, 0.35562825202941895, 0.5311083197593689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2274796962738037})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5606212615966797})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42769694328308105})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33788779377937317})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31768620014190674})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2986794710159302})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31475287675857544})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2711222469806671})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2946714162826538})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.268582820892334})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2800101637840271})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29938003420829773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28977686166763306})
store['active_learning_steps'][21]['training']['best_epoch']=10
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2405501953125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 42140], ['id', 58874], ['id', 57018], ['id', 51964], ['id', 43897], ['id', 14528], ['id', 99], ['id', 17958], ['id', 54628], ['id', 32426], ['id', 47321], ['id', 13452], ['id', 13878], ['id', 52892], ['id', 12986], ['id', 42702], ['id', 53017], ['id', 35774], ['id', 37758], ['id', 52953]], 'labels': [3, 3, 9, 8, 1, 4, 1, 9, 4, 8, 2, 2, 4, 8, 5, 1, 2, 1, 0, 2], 'scores': [0.9623517394065857, 0.6692545413970947, 0.9049571752548218, 0.5498323142528534, 0.7920762300491333, 0.8338510990142822, 0.3919704556465149, 0.7874671220779419, 0.839149534702301, 0.6544613838195801, 0.8817035555839539, 0.3111306428909302, 0.8513529896736145, 0.7475467026233673, 0.7365599870681763, 0.6050688028335571, 0.8886314630508423, 0.43725940585136414, 0.533321738243103, 0.906029462814331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0149176120758057})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.570898175239563})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39933598041534424})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3513975441455841})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2896844744682312})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29582902789115906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28561192750930786})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28478431701660156})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25436368584632874})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2514333724975586})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2856117784976959})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2738662660121918})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27908432483673096})
store['active_learning_steps'][22]['training']['best_epoch']=10
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2376389892578125}
